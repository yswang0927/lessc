# coding=utf-8
# LESS compiler for Sublime Text 3 in windows
# author: yswang
# version: 0.1-2015/02/05
# Licensed under the MIT

import os
import sys
import re
import pdb
import subprocess
import functools
import sublime
import sublime_plugin


package_name = 'lessc'

CFG_LESS_DIR='less_dir'
CFG_OUTPUT_DIR='output_dir'
CFG_AUTO_COMPILE='auto_compile'
CFG_COMPRESS='compress'
CFG_ENCODING='encoding'
DEF_ENCODING='UTF-8'

#get lessc setting
def getSetting():
  # default settings
  config = sublime.load_settings('lessc.sublime-settings')
  # load project htmlc settings
  project_config = sublime.active_window().active_view().settings().get("lessc")
  if project_config is None:
    project_config = {}

  return {
    'less_dir': normalizePath(project_config.get(CFG_LESS_DIR, config.get(CFG_LESS_DIR, ''))),
    'output_dir': normalizePath(project_config.get(CFG_OUTPUT_DIR, config.get(CFG_OUTPUT_DIR, ''))),
    'auto_compile': project_config.get(CFG_AUTO_COMPILE, config.get(CFG_AUTO_COMPILE, True)),
    'compress': project_config.get(CFG_COMPRESS, config.get(CFG_COMPRESS, False)),
    'encoding': project_config.get(CFG_ENCODING, config.get(CFG_ENCODING, DEF_ENCODING))
  }

# compile all less files in current less dir 
def lesscAll():
  cfg = getSetting()
  _less_dir = cfg[CFG_LESS_DIR]
  if (os.path.exists(_less_dir)==False):
    return
  # list all less files
  for root, dirs, files in os.walk(_less_dir):
    for filepath in files:
      lessc(os.path.join(root, filepath))


# less file to css
def lessc(filepath):
  if filepath is None:
    return

  (fileroot, fileext) = os.path.splitext(filepath)
  if (fileext!='.less'):
    return

  cfg = getSetting()
  _less_dir=cfg[CFG_LESS_DIR]
  _output_dir=cfg[CFG_OUTPUT_DIR]
  _is_compress=cfg[CFG_AUTO_COMPILE]
  _encoding=cfg[CFG_ENCODING]

  (less_file_dir, less_file_name)=os.path.split(filepath)

  if _less_dir=='':
    _less_dir=less_file_dir

  if _output_dir=='':
    _output_dir=less_file_dir

  # relative path from current file path
  if (_output_dir.startswith('./') or _output_dir.startswith('../') or _output_dir.startswith('.\\') or _output_dir.startswith('..\\')):
    _output_dir=os.path.join(less_file_dir, _output_dir)

  # parse relative path: ./ ../ if exists
  _output_dir=os.path.normpath(_output_dir)

  if os.path.exists(_less_dir)==False:
    sublime.error_message('The less dir "'+ _less_dir +'" is not exists!')

  if os.path.exists(_output_dir)==False:
    os.makedirs(_output_dir)

  less_file_subdir=''
  if less_file_dir.startswith(_less_dir):
    # delete the less dir prevfix path
    less_file_subdir=less_file_dir[len(_less_dir)+1:]

  # make the absolute output dirs if not exists
  output_abpath=os.path.join(_output_dir, less_file_subdir)
  if os.path.exists(output_abpath)==False:
    os.makedirs(output_abpath)

  (fname, fext)=os.path.splitext(less_file_name)
  output_file=os.path.join(output_abpath, fname+'.css')

  execmd = '@cscript //nologo "'+sublime.packages_path()+'\\'+package_name+'\\lessc.wsf"'+' "'+ filepath +'"'+' "'+ output_file +'"'

  if _is_compress:
    execmd += ' -compress'

  execmd += ' --encoding=' + _encoding

  #execmd = execmd.encode(_encoding) #先将编码转换到gbk

  res = subprocess.Popen(execmd, bufsize=-1, executable=None, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=None, close_fds=False, shell=True)
  res.wait()

  error = res.stderr.read()
  remsg = '';
  if error==b'':
    remsg = ' O(∩_∩)O~ ** Compiled success: '+ output_file +' ** O(∩_∩)O~'
  else:
    #errorinfo = error.split(b"\r\n")
    remsg = error.decode('gbk')
    sublime.error_message('Error: Failed less['+filepath+'] to css! '+ remsg)

  sublime.set_timeout(functools.partial(status, remsg), 1200);
  sublime.set_timeout(functools.partial(reloadCss, output_file), 400);
    

def normalizePath(path):
  if (path.endswith(os.sep)):
    path=path[:-1]
  return path

def status(msg):
  sublime.status_message(msg)


#reload the opened css file
def reloadCss(cssfile):
  cfg=getSetting()
  for win in sublime.windows():
    for view in win.views():
      if(view.file_name()==cssfile):
        view.run_command("reopen", {"encoding": cfg[CFG_ENCODING]})


#Compile current less file to html
class LessToCssCommand(sublime_plugin.TextCommand):
  def run(self, text):
    filepath = self.view.file_name()
    if filepath is None:
      return
    lessc(filepath)


#Compile all less files to html in current project
class AllLessToCssCommand(sublime_plugin.TextCommand):
  def run(self, text):
    lesscAll()

#Auto lessc to css on saved
class AutoLessToCssSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    cfg = getSetting()
    if cfg[CFG_AUTO_COMPILE]:
      view.run_command("less_to_css")