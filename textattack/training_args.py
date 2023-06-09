Run sudo sed -i 's/azure\.//' /etc/apt/sources.list # workaround for flaky pandoc install
Get:1 https://packages.microsoft.com/ubuntu/22.04/prod jammy InRelease [3611 B]
Get:2 https://packages.microsoft.com/ubuntu/22.04/prod jammy/main arm64 Packages [14.3 kB]
Get:3 https://packages.microsoft.com/ubuntu/22.04/prod jammy/main armhf Packages [7418 B]
Get:4 https://packages.microsoft.com/ubuntu/22.04/prod jammy/main amd64 Packages [66.1 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Hit:6 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu jammy InRelease
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [108 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1395 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/main Translation-en [510 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/main amd64 c-n-f Metadata [30.3 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [129 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy/restricted Translation-en [18.6 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 c-n-f Metadata [488 B]
Get:16 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [14.1 MB]
Get:17 http://archive.ubuntu.com/ubuntu jammy/universe Translation-en [5652 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy/universe amd64 c-n-f Metadata [286 kB]
Get:19 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [217 kB]
Get:20 http://archive.ubuntu.com/ubuntu jammy/multiverse Translation-en [112 kB]
Get:21 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 c-n-f Metadata [8372 B]
Get:22 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [672 kB]
Get:23 http://archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [182 kB]
Get:24 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 c-n-f Metadata [15.0 kB]
Get:25 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [350 kB]
Get:26 http://archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [52.8 kB]
Get:27 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 c-n-f Metadata [604 B]
Get:28 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [920 kB]
Get:29 http://archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [194 kB]
Get:30 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 c-n-f Metadata [20.0 kB]
Get:31 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [35.3 kB]
Get:32 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse Translation-en [8452 B]
Get:33 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 c-n-f Metadata [468 B]
Get:34 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [40.9 kB]
Get:35 http://archive.ubuntu.com/ubuntu jammy-backports/main Translation-en [10.2 kB]
Get:36 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 c-n-f Metadata [388 B]
Get:37 http://archive.ubuntu.com/ubuntu jammy-backports/restricted amd64 c-n-f Metadata [116 B]
Get:38 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [23.4 kB]
Get:39 http://archive.ubuntu.com/ubuntu jammy-backports/universe Translation-en [15.0 kB]
Get:40 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 c-n-f Metadata [548 B]
Get:41 http://archive.ubuntu.com/ubuntu jammy-backports/multiverse amd64 c-n-f Metadata [116 B]
Get:42 http://archive.ubuntu.com/ubuntu jammy-security/main amd64 Packages [455 kB]
Get:43 http://archive.ubuntu.com/ubuntu jammy-security/main Translation-en [122 kB]
Get:44 http://archive.ubuntu.com/ubuntu jammy-security/main amd64 c-n-f Metadata [10.1 kB]
Get:45 http://archive.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [349 kB]
Get:46 http://archive.ubuntu.com/ubuntu jammy-security/restricted Translation-en [52.6 kB]
Get:47 http://archive.ubuntu.com/ubuntu jammy-security/restricted amd64 c-n-f Metadata [604 B]
Get:48 http://archive.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [732 kB]
Get:49 http://archive.ubuntu.com/ubuntu jammy-security/universe Translation-en [129 kB]
Get:50 http://archive.ubuntu.com/ubuntu jammy-security/universe amd64 c-n-f Metadata [15.6 kB]
Get:51 http://archive.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [30.2 kB]
Get:52 http://archive.ubuntu.com/ubuntu jammy-security/multiverse Translation-en [5828 B]
Get:53 http://archive.ubuntu.com/ubuntu jammy-security/multiverse amd64 c-n-f Metadata [252 B]
Fetched 27.6 MB in 11s (2614 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libcmark-gfm-extensions0.29.0.gfm.3 libcmark-gfm0.29.0.gfm.3 pandoc-data
Suggested packages:
  texlive-latex-recommended texlive-xetex texlive-luatex pandoc-citeproc
  texlive-latex-extra context wkhtmltopdf librsvg2-bin groff ghc nodejs python
  libjs-mathjax libjs-katex citation-style-language-styles
The following NEW packages will be installed:
  libcmark-gfm-extensions0.29.0.gfm.3 libcmark-gfm0.29.0.gfm.3 pandoc
  pandoc-data
0 upgraded, 4 newly installed, 0 to remove and 109 not upgraded.
Need to get 20.6 MB of archives.
After this operation, 156 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libcmark-gfm0.29.0.gfm.3 amd64 0.29.0.gfm.3-3 [115 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/universe amd64 libcmark-gfm-extensions0.29.0.gfm.3 amd64 0.29.0.gfm.3-3 [25.1 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/universe amd64 pandoc-data all 2.9.2.1-3ubuntu2 [81.8 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy/universe amd64 pandoc amd64 2.9.2.1-3ubuntu2 [20.3 MB]
Fetched 20.6 MB in 2s (9659 kB/s)
Selecting previously unselected package libcmark-gfm0.29.0.gfm.3:amd64.
(Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 222303 files and directories currently installed.)
Preparing to unpack .../libcmark-gfm0.29.0.gfm.3_0.29.0.gfm.3-3_amd64.deb ...
Unpacking libcmark-gfm0.29.0.gfm.3:amd64 (0.29.0.gfm.3-3) ...
Selecting previously unselected package libcmark-gfm-extensions0.29.0.gfm.3:amd64.
Preparing to unpack .../libcmark-gfm-extensions0.29.0.gfm.3_0.29.0.gfm.3-3_amd64.deb ...
Unpacking libcmark-gfm-extensions0.29.0.gfm.3:amd64 (0.29.0.gfm.3-3) ...
Selecting previously unselected package pandoc-data.
Preparing to unpack .../pandoc-data_2.9.2.1-3ubuntu2_all.deb ...
Unpacking pandoc-data (2.9.2.1-3ubuntu2) ...
Selecting previously unselected package pandoc.
Preparing to unpack .../pandoc_2.9.2.1-3ubuntu2_amd64.deb ...
Unpacking pandoc (2.9.2.1-3ubuntu2) ...
Setting up libcmark-gfm0.29.0.gfm.3:amd64 (0.29.0.gfm.3-3) ...
Setting up libcmark-gfm-extensions0.29.0.gfm.3:amd64 (0.29.0.gfm.3-3) ...
Setting up pandoc-data (2.9.2.1-3ubuntu2) ...
Setting up pandoc (2.9.2.1-3ubuntu2) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
NEEDRESTART-VER: 3.5
NEEDRESTART-KCUR: 5.15.0-1038-azure
NEEDRESTART-KEXP: 5.15.0-1038-azure
NEEDRESTART-KSTA: 1
Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (22.0.4)
Collecting pip
  Downloading pip-23.1.2-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 12.9 MB/s eta 0:00:00
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (56.0.0)
Collecting setuptools
  Downloading setuptools-67.8.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 24.5 MB/s eta 0:00:00
Collecting wheel
  Downloading wheel-0.40.0-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.5/64.5 kB 24.6 MB/s eta 0:00:00
Installing collected packages: wheel, setuptools, pip
  Attempting uninstall: setuptools
    Found existing installation: setuptools 56.0.0
    Uninstalling setuptools-56.0.0:
      Successfully uninstalled setuptools-56.0.0
  Attempting uninstall: pip
    Found existing installation: pip 22.0.4
    Uninstalling pip-22.0.4:
      Successfully uninstalled pip-22.0.4
Successfully installed pip-23.1.2 setuptools-67.8.0 wheel-0.40.0
Collecting ipython
  Downloading ipython-8.12.2-py3-none-any.whl (797 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 797.8/797.8 kB 13.1 MB/s eta 0:00:00
Collecting backcall (from ipython)
  Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting decorator (from ipython)
  Downloading decorator-5.1.1-py3-none-any.whl (9.1 kB)
Collecting jedi>=0.16 (from ipython)
  Downloading jedi-0.18.2-py2.py3-none-any.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 25.4 MB/s eta 0:00:00
Collecting matplotlib-inline (from ipython)
  Downloading matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
Collecting pickleshare (from ipython)
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 (from ipython)
  Downloading prompt_toolkit-3.0.38-py3-none-any.whl (385 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 385.8/385.8 kB 32.0 MB/s eta 0:00:00
Collecting pygments>=2.4.0 (from ipython)
  Downloading Pygments-2.15.1-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 33.7 MB/s eta 0:00:00
Collecting stack-data (from ipython)
  Downloading stack_data-0.6.2-py3-none-any.whl (24 kB)
Collecting traitlets>=5 (from ipython)
  Downloading traitlets-5.9.0-py3-none-any.whl (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.4/117.4 kB 44.5 MB/s eta 0:00:00
Collecting typing-extensions (from ipython)
  Downloading typing_extensions-4.6.3-py3-none-any.whl (31 kB)
Collecting pexpect>4.3 (from ipython)
  Downloading pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.0/59.0 kB 22.8 MB/s eta 0:00:00
Collecting parso<0.9.0,>=0.8.0 (from jedi>=0.16->ipython)
  Downloading parso-0.8.3-py2.py3-none-any.whl (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.8/100.8 kB 40.8 MB/s eta 0:00:00
Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython)
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Collecting wcwidth (from prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30->ipython)
  Downloading wcwidth-0.2.6-py2.py3-none-any.whl (29 kB)
Collecting executing>=1.2.0 (from stack-data->ipython)
  Downloading executing-1.2.0-py2.py3-none-any.whl (24 kB)
Collecting asttokens>=2.1.0 (from stack-data->ipython)
  Downloading asttokens-2.2.1-py2.py3-none-any.whl (26 kB)
Collecting pure-eval (from stack-data->ipython)
  Downloading pure_eval-0.2.2-py3-none-any.whl (11 kB)
Collecting six (from asttokens>=2.1.0->stack-data->ipython)
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: wcwidth, pure-eval, ptyprocess, pickleshare, executing, backcall, typing-extensions, traitlets, six, pygments, prompt-toolkit, pexpect, parso, decorator, matplotlib-inline, jedi, asttokens, stack-data, ipython
Successfully installed asttokens-2.2.1 backcall-0.2.0 decorator-5.1.1 executing-1.2.0 ipython-8.12.2 jedi-0.18.2 matplotlib-inline-0.1.6 parso-0.8.3 pexpect-4.8.0 pickleshare-0.7.5 prompt-toolkit-3.0.38 ptyprocess-0.7.0 pure-eval-0.2.2 pygments-2.15.1 six-1.16.0 stack-data-0.6.2 traitlets-5.9.0 typing-extensions-4.6.3 wcwidth-0.2.6
running install_egg_info
running egg_info
creating textattack.egg-info
writing textattack.egg-info/PKG-INFO
writing dependency_links to textattack.egg-info/dependency_links.txt
writing entry points to textattack.egg-info/entry_points.txt
writing requirements to textattack.egg-info/requires.txt
writing top-level names to textattack.egg-info/top_level.txt
writing manifest file 'textattack.egg-info/SOURCES.txt'
reading manifest file 'textattack.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'textattack.egg-info/SOURCES.txt'
Copying textattack.egg-info to /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages/textattack-0.3.8-py3.8.egg-info
/opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer, pypa/build or
        other standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
Obtaining file:///home/runner/work/TextAttack/TextAttack
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting bert-score>=0.3.5 (from textattack==0.3.8)
  Downloading bert_score-0.3.13-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.1/61.1 kB 2.4 MB/s eta 0:00:00
Collecting editdistance (from textattack==0.3.8)
  Downloading editdistance-0.6.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (283 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 283.4/283.4 kB 9.3 MB/s eta 0:00:00
Collecting flair (from textattack==0.3.8)
  Downloading flair-0.12.2-py3-none-any.whl (373 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 373.1/373.1 kB 12.2 MB/s eta 0:00:00
Collecting filelock (from textattack==0.3.8)
  Downloading filelock-3.12.0-py3-none-any.whl (10 kB)
Collecting language_tool_python (from textattack==0.3.8)
  Downloading language_tool_python-2.7.1-py3-none-any.whl (34 kB)
Collecting lemminflect (from textattack==0.3.8)
  Downloading lemminflect-0.2.3-py3-none-any.whl (769 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 769.7/769.7 kB 15.1 MB/s eta 0:00:00
Collecting lru-dict (from textattack==0.3.8)
  Downloading lru_dict-1.2.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (29 kB)
Collecting datasets==2.4.0 (from textattack==0.3.8)
  Downloading datasets-2.4.0-py3-none-any.whl (365 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 365.7/365.7 kB 17.4 MB/s eta 0:00:00
Collecting nltk (from textattack==0.3.8)
  Downloading nltk-3.8.1-py3-none-any.whl (1.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 22.8 MB/s eta 0:00:00
Collecting numpy>=1.21.0 (from textattack==0.3.8)
  Downloading numpy-1.24.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.3/17.3 MB 72.2 MB/s eta 0:00:00
Collecting pandas>=1.0.1 (from textattack==0.3.8)
  Downloading pandas-2.0.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 112.8 MB/s eta 0:00:00
Collecting scipy>=1.4.1 (from textattack==0.3.8)
  Downloading scipy-1.10.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (34.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 34.5/34.5 MB 74.5 MB/s eta 0:00:00
Collecting torch!=1.8,>=1.7.0 (from textattack==0.3.8)
  Downloading torch-2.0.1-cp38-cp38-manylinux1_x86_64.whl (619.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 619.9/619.9 MB 1.6 MB/s eta 0:00:00
Collecting transformers>=4.21.0 (from textattack==0.3.8)
  Downloading transformers-4.30.0-py3-none-any.whl (7.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 110.0 MB/s eta 0:00:00
Collecting terminaltables (from textattack==0.3.8)
  Downloading terminaltables-3.1.10-py2.py3-none-any.whl (15 kB)
Collecting tqdm (from textattack==0.3.8)
  Downloading tqdm-4.65.0-py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.1/77.1 kB 28.1 MB/s eta 0:00:00
Collecting word2number (from textattack==0.3.8)
  Downloading word2number-1.1.zip (9.7 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting num2words (from textattack==0.3.8)
  Downloading num2words-0.5.12-py3-none-any.whl (125 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.2/125.2 kB 44.2 MB/s eta 0:00:00
Collecting more-itertools (from textattack==0.3.8)
  Downloading more_itertools-9.1.0-py3-none-any.whl (54 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.2/54.2 kB 24.3 MB/s eta 0:00:00
Collecting PySocks!=1.5.7,>=1.5.6 (from textattack==0.3.8)
  Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
Collecting pinyin==0.4.0 (from textattack==0.3.8)
  Downloading pinyin-0.4.0.tar.gz (3.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 104.6 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting jieba (from textattack==0.3.8)
  Downloading jieba-0.42.1.tar.gz (19.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.2/19.2 MB 68.6 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting OpenHowNet (from textattack==0.3.8)
  Downloading OpenHowNet-2.0-py3-none-any.whl (18 kB)
Collecting pycld2 (from textattack==0.3.8)
  Downloading pycld2-0.41.tar.gz (41.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.4/41.4 MB 51.6 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting click<8.1.0 (from textattack==0.3.8)
  Downloading click-8.0.4-py3-none-any.whl (97 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.5/97.5 kB 32.6 MB/s eta 0:00:00
Collecting recommonmark (from textattack==0.3.8)
  Downloading recommonmark-0.7.1-py2.py3-none-any.whl (10 kB)
Collecting nbsphinx (from textattack==0.3.8)
  Downloading nbsphinx-0.9.2-py3-none-any.whl (30 kB)
Collecting sphinx-autobuild (from textattack==0.3.8)
  Downloading sphinx_autobuild-2021.3.14-py3-none-any.whl (9.9 kB)
Collecting sphinx-rtd-theme (from textattack==0.3.8)
  Downloading sphinx_rtd_theme-1.2.2-py2.py3-none-any.whl (2.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 108.2 MB/s eta 0:00:00
Collecting sphinx-markdown-tables (from textattack==0.3.8)
  Downloading sphinx_markdown_tables-0.0.17-py3-none-any.whl (28 kB)
Collecting sphinx-copybutton (from textattack==0.3.8)
  Downloading sphinx_copybutton-0.5.2-py3-none-any.whl (13 kB)
Collecting black==20.8b1 (from textattack==0.3.8)
  Downloading black-20.8b1.tar.gz (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 111.1 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting docformatter (from textattack==0.3.8)
  Downloading docformatter-1.7.2-py3-none-any.whl (32 kB)
Collecting isort==5.6.4 (from textattack==0.3.8)
  Downloading isort-5.6.4-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.9/98.9 kB 40.0 MB/s eta 0:00:00
Collecting flake8 (from textattack==0.3.8)
  Downloading flake8-6.0.0-py2.py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.8/57.8 kB 24.2 MB/s eta 0:00:00
Collecting pytest (from textattack==0.3.8)
  Downloading pytest-7.3.1-py3-none-any.whl (320 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 320.5/320.5 kB 76.7 MB/s eta 0:00:00
Collecting pytest-xdist (from textattack==0.3.8)
  Downloading pytest_xdist-3.3.1-py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.8/41.8 kB 17.3 MB/s eta 0:00:00
Collecting tensorflow==2.9.1 (from textattack==0.3.8)
  Downloading tensorflow-2.9.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (511.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 511.7/511.7 MB 2.1 MB/s eta 0:00:00
Collecting tensorflow_hub (from textattack==0.3.8)
  Downloading tensorflow_hub-0.13.0-py2.py3-none-any.whl (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.6/100.6 kB 40.7 MB/s eta 0:00:00
Collecting tensorflow_text>=2 (from textattack==0.3.8)
  Downloading tensorflow_text-2.12.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 109.9 MB/s eta 0:00:00
Collecting tensorboardX (from textattack==0.3.8)
  Downloading tensorboardX-2.6-py2.py3-none-any.whl (114 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.5/114.5 kB 42.3 MB/s eta 0:00:00
Collecting tensorflow-estimator==2.9.0 (from textattack==0.3.8)
  Downloading tensorflow_estimator-2.9.0-py2.py3-none-any.whl (438 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 438.7/438.7 kB 91.2 MB/s eta 0:00:00
Collecting sentence_transformers==2.2.0 (from textattack==0.3.8)
  Downloading sentence-transformers-2.2.0.tar.gz (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.7/79.7 kB 34.1 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting stanza (from textattack==0.3.8)
  Downloading stanza-1.5.0-py3-none-any.whl (802 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 802.5/802.5 kB 109.0 MB/s eta 0:00:00
Collecting visdom (from textattack==0.3.8)
  Downloading visdom-0.2.4.tar.gz (1.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 103.3 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting wandb (from textattack==0.3.8)
  Downloading wandb-0.15.4-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 111.2 MB/s eta 0:00:00
Collecting gensim==4.1.2 (from textattack==0.3.8)
  Downloading gensim-4.1.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (24.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.1/24.1 MB 44.2 MB/s eta 0:00:00
Collecting appdirs (from black==20.8b1->textattack==0.3.8)
  Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Collecting toml>=0.10.1 (from black==20.8b1->textattack==0.3.8)
  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting typed-ast>=1.4.0 (from black==20.8b1->textattack==0.3.8)
  Downloading typed_ast-1.5.4-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (897 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 897.2/897.2 kB 109.7 MB/s eta 0:00:00
Collecting regex>=2020.1.8 (from black==20.8b1->textattack==0.3.8)
  Downloading regex-2023.6.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (772 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 772.3/772.3 kB 103.9 MB/s eta 0:00:00
Collecting pathspec<1,>=0.6 (from black==20.8b1->textattack==0.3.8)
  Downloading pathspec-0.11.1-py3-none-any.whl (29 kB)
Requirement already satisfied: typing-extensions>=3.7.4 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from black==20.8b1->textattack==0.3.8) (4.6.3)
Collecting mypy-extensions>=0.4.3 (from black==20.8b1->textattack==0.3.8)
  Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Collecting pyarrow>=6.0.0 (from datasets==2.4.0->textattack==0.3.8)
  Downloading pyarrow-12.0.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (39.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.0/39.0 MB 60.5 MB/s eta 0:00:00
Collecting dill<0.3.6 (from datasets==2.4.0->textattack==0.3.8)
  Downloading dill-0.3.5.1-py2.py3-none-any.whl (95 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.8/95.8 kB 35.5 MB/s eta 0:00:00
Collecting requests>=2.19.0 (from datasets==2.4.0->textattack==0.3.8)
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 24.6 MB/s eta 0:00:00
Collecting xxhash (from datasets==2.4.0->textattack==0.3.8)
  Downloading xxhash-3.2.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (213 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 213.0/213.0 kB 61.2 MB/s eta 0:00:00
Collecting multiprocess (from datasets==2.4.0->textattack==0.3.8)
  Downloading multiprocess-0.70.14-py38-none-any.whl (132 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 132.0/132.0 kB 52.6 MB/s eta 0:00:00
Collecting fsspec[http]>=2021.11.1 (from datasets==2.4.0->textattack==0.3.8)
  Downloading fsspec-2023.5.0-py3-none-any.whl (160 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.1/160.1 kB 61.4 MB/s eta 0:00:00
Collecting aiohttp (from datasets==2.4.0->textattack==0.3.8)
  Downloading aiohttp-3.8.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 115.8 MB/s eta 0:00:00
Collecting huggingface-hub<1.0.0,>=0.1.0 (from datasets==2.4.0->textattack==0.3.8)
  Downloading huggingface_hub-0.15.1-py3-none-any.whl (236 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 236.8/236.8 kB 69.6 MB/s eta 0:00:00
Collecting packaging (from datasets==2.4.0->textattack==0.3.8)
  Using cached packaging-23.1-py3-none-any.whl (48 kB)
Collecting responses<0.19 (from datasets==2.4.0->textattack==0.3.8)
  Downloading responses-0.18.0-py3-none-any.whl (38 kB)
Collecting smart-open>=1.8.1 (from gensim==4.1.2->textattack==0.3.8)
  Downloading smart_open-6.3.0-py3-none-any.whl (56 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.8/56.8 kB 23.7 MB/s eta 0:00:00
Collecting torchvision (from sentence_transformers==2.2.0->textattack==0.3.8)
  Downloading torchvision-0.15.2-cp38-cp38-manylinux1_x86_64.whl (33.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 33.8/33.8 MB 57.3 MB/s eta 0:00:00
Collecting scikit-learn (from sentence_transformers==2.2.0->textattack==0.3.8)
  Downloading scikit_learn-1.2.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (9.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.8/9.8 MB 86.2 MB/s eta 0:00:00
Collecting sentencepiece (from sentence_transformers==2.2.0->textattack==0.3.8)
  Downloading sentencepiece-0.1.99-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 89.2 MB/s eta 0:00:00
Collecting absl-py>=1.0.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading absl_py-1.4.0-py3-none-any.whl (126 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 126.5/126.5 kB 51.0 MB/s eta 0:00:00
Collecting astunparse>=1.6.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Collecting flatbuffers<2,>=1.12 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading flatbuffers-1.12-py2.py3-none-any.whl (15 kB)
Collecting gast<=0.4.0,>=0.2.1 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading gast-0.4.0-py3-none-any.whl (9.8 kB)
Collecting google-pasta>=0.1.1 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 24.5 MB/s eta 0:00:00
Collecting grpcio<2.0,>=1.24.3 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading grpcio-1.54.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 88.3 MB/s eta 0:00:00
Collecting h5py>=2.9.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading h5py-3.8.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 93.9 MB/s eta 0:00:00
Collecting keras<2.10.0,>=2.9.0rc0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading keras-2.9.0-py2.py3-none-any.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 90.9 MB/s eta 0:00:00
Collecting keras-preprocessing>=1.1.1 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.6/42.6 kB 19.1 MB/s eta 0:00:00
Collecting libclang>=13.0.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading libclang-16.0.0-py2.py3-none-manylinux2010_x86_64.whl (22.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.9/22.9 MB 72.9 MB/s eta 0:00:00
Collecting opt-einsum>=2.3.2 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.5/65.5 kB 25.3 MB/s eta 0:00:00
Collecting protobuf<3.20,>=3.9.2 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading protobuf-3.19.6-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 90.6 MB/s eta 0:00:00
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from tensorflow==2.9.1->textattack==0.3.8) (67.8.0)
Requirement already satisfied: six>=1.12.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from tensorflow==2.9.1->textattack==0.3.8) (1.16.0)
Collecting tensorboard<2.10,>=2.9 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading tensorboard-2.9.1-py3-none-any.whl (5.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 97.2 MB/s eta 0:00:00
Collecting tensorflow-io-gcs-filesystem>=0.23.1 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading tensorflow_io_gcs_filesystem-0.32.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (2.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 96.1 MB/s eta 0:00:00
Collecting termcolor>=1.1.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading termcolor-2.3.0-py3-none-any.whl (6.9 kB)
Collecting wrapt>=1.11.0 (from tensorflow==2.9.1->textattack==0.3.8)
  Downloading wrapt-1.15.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (81 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 81.5/81.5 kB 29.2 MB/s eta 0:00:00
Collecting matplotlib (from bert-score>=0.3.5->textattack==0.3.8)
  Downloading matplotlib-3.7.1-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (9.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 92.6 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2 (from pandas>=1.0.1->textattack==0.3.8)
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 69.9 MB/s eta 0:00:00
Collecting pytz>=2020.1 (from pandas>=1.0.1->textattack==0.3.8)
  Downloading pytz-2023.3-py2.py3-none-any.whl (502 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 502.3/502.3 kB 94.0 MB/s eta 0:00:00
Collecting tzdata>=2022.1 (from pandas>=1.0.1->textattack==0.3.8)
  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 341.8/341.8 kB 76.8 MB/s eta 0:00:00
INFO: pip is looking at multiple versions of tensorflow-text to determine which version is compatible with other requirements. This could take a while.
Collecting tensorflow_text>=2 (from textattack==0.3.8)
  Downloading tensorflow_text-2.12.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 93.7 MB/s eta 0:00:00
  Downloading tensorflow_text-2.11.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 95.2 MB/s eta 0:00:00
  Downloading tensorflow_text-2.10.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.9/5.9 MB 85.3 MB/s eta 0:00:00
  Downloading tensorflow_text-2.9.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 95.1 MB/s eta 0:00:00
Collecting sympy (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading sympy-1.12-py3-none-any.whl (5.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 96.8 MB/s eta 0:00:00
Collecting networkx (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading networkx-3.1-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 91.9 MB/s eta 0:00:00
Collecting jinja2 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 53.6 MB/s eta 0:00:00
Collecting nvidia-cuda-nvrtc-cu11==11.7.99 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cuda_nvrtc_cu11-11.7.99-2-py3-none-manylinux1_x86_64.whl (21.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.0/21.0 MB 77.0 MB/s eta 0:00:00
Collecting nvidia-cuda-runtime-cu11==11.7.99 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cuda_runtime_cu11-11.7.99-py3-none-manylinux1_x86_64.whl (849 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 849.3/849.3 kB 104.0 MB/s eta 0:00:00
Collecting nvidia-cuda-cupti-cu11==11.7.101 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cuda_cupti_cu11-11.7.101-py3-none-manylinux1_x86_64.whl (11.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.8/11.8 MB 93.9 MB/s eta 0:00:00
Collecting nvidia-cudnn-cu11==8.5.0.96 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cudnn_cu11-8.5.0.96-2-py3-none-manylinux1_x86_64.whl (557.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 557.1/557.1 MB 1.7 MB/s eta 0:00:00
Collecting nvidia-cublas-cu11==11.10.3.66 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cublas_cu11-11.10.3.66-py3-none-manylinux1_x86_64.whl (317.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 317.1/317.1 MB 3.8 MB/s eta 0:00:00
Collecting nvidia-cufft-cu11==10.9.0.58 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cufft_cu11-10.9.0.58-py3-none-manylinux1_x86_64.whl (168.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 168.4/168.4 MB 6.0 MB/s eta 0:00:00
Collecting nvidia-curand-cu11==10.2.10.91 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_curand_cu11-10.2.10.91-py3-none-manylinux1_x86_64.whl (54.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.6/54.6 MB 43.4 MB/s eta 0:00:00
Collecting nvidia-cusolver-cu11==11.4.0.1 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cusolver_cu11-11.4.0.1-2-py3-none-manylinux1_x86_64.whl (102.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 102.6/102.6 MB 24.6 MB/s eta 0:00:00
Collecting nvidia-cusparse-cu11==11.7.4.91 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_cusparse_cu11-11.7.4.91-py3-none-manylinux1_x86_64.whl (173.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 173.2/173.2 MB 2.9 MB/s eta 0:00:00
Collecting nvidia-nccl-cu11==2.14.3 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_nccl_cu11-2.14.3-py3-none-manylinux1_x86_64.whl (177.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 177.1/177.1 MB 9.6 MB/s eta 0:00:00
Collecting nvidia-nvtx-cu11==11.7.91 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading nvidia_nvtx_cu11-11.7.91-py3-none-manylinux1_x86_64.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.6/98.6 kB 39.5 MB/s eta 0:00:00
Collecting triton==2.0.0 (from torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading triton-2.0.0-1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (63.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.2/63.2 MB 41.5 MB/s eta 0:00:00
Requirement already satisfied: wheel in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nvidia-cublas-cu11==11.10.3.66->torch!=1.8,>=1.7.0->textattack==0.3.8) (0.40.0)
Collecting cmake (from triton==2.0.0->torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading cmake-3.26.4-py2.py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (24.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.0/24.0 MB 85.2 MB/s eta 0:00:00
Collecting lit (from triton==2.0.0->torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading lit-16.0.5.post0.tar.gz (138 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 138.1/138.1 kB 51.0 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting pyyaml>=5.1 (from transformers>=4.21.0->textattack==0.3.8)
  Downloading PyYAML-6.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (701 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 701.2/701.2 kB 96.9 MB/s eta 0:00:00
Collecting tokenizers!=0.11.3,<0.14,>=0.11.1 (from transformers>=4.21.0->textattack==0.3.8)
  Downloading tokenizers-0.13.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.8/7.8 MB 104.9 MB/s eta 0:00:00
Collecting safetensors>=0.3.1 (from transformers>=4.21.0->textattack==0.3.8)
  Downloading safetensors-0.3.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 98.2 MB/s eta 0:00:00
Collecting charset_normalizer<4.0.0,>=3.0.0 (from docformatter->textattack==0.3.8)
  Downloading charset_normalizer-3.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (195 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 195.9/195.9 kB 61.4 MB/s eta 0:00:00
Collecting untokenize<0.2.0,>=0.1.1 (from docformatter->textattack==0.3.8)
  Downloading untokenize-0.1.1.tar.gz (3.1 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting segtok>=1.5.7 (from flair->textattack==0.3.8)
  Downloading segtok-1.5.11-py3-none-any.whl (24 kB)
Collecting mpld3==0.3 (from flair->textattack==0.3.8)
  Downloading mpld3-0.3.tar.gz (788 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 788.5/788.5 kB 99.1 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting sqlitedict>=1.6.0 (from flair->textattack==0.3.8)
  Downloading sqlitedict-2.1.0.tar.gz (21 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting deprecated>=1.2.4 (from flair->textattack==0.3.8)
  Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)
Collecting hyperopt>=0.2.7 (from flair->textattack==0.3.8)
  Downloading hyperopt-0.2.7-py2.py3-none-any.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 72.4 MB/s eta 0:00:00
Collecting boto3 (from flair->textattack==0.3.8)
  Downloading boto3-1.26.150-py3-none-any.whl (135 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 135.6/135.6 kB 46.0 MB/s eta 0:00:00
Collecting bpemb>=0.3.2 (from flair->textattack==0.3.8)
  Downloading bpemb-0.3.4-py3-none-any.whl (19 kB)
Collecting tabulate (from flair->textattack==0.3.8)
  Downloading tabulate-0.9.0-py3-none-any.whl (35 kB)
Collecting langdetect (from flair->textattack==0.3.8)
  Downloading langdetect-1.0.9.tar.gz (981 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 981.5/981.5 kB 97.5 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting lxml (from flair->textattack==0.3.8)
  Downloading lxml-4.9.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 82.7 MB/s eta 0:00:00
Collecting ftfy (from flair->textattack==0.3.8)
  Downloading ftfy-6.1.1-py3-none-any.whl (53 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.1/53.1 kB 24.1 MB/s eta 0:00:00
Collecting janome (from flair->textattack==0.3.8)
  Downloading Janome-0.4.2-py2.py3-none-any.whl (19.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.7/19.7 MB 85.8 MB/s eta 0:00:00
Collecting gdown==4.4.0 (from flair->textattack==0.3.8)
  Downloading gdown-4.4.0.tar.gz (14 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting conllu>=4.0 (from flair->textattack==0.3.8)
  Downloading conllu-4.5.2-py2.py3-none-any.whl (16 kB)
Collecting wikipedia-api (from flair->textattack==0.3.8)
  Downloading Wikipedia_API-0.5.8-py3-none-any.whl (13 kB)
Collecting pptree (from flair->textattack==0.3.8)
  Downloading pptree-3.1.tar.gz (3.0 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting pytorch-revgrad (from flair->textattack==0.3.8)
  Downloading pytorch_revgrad-0.2.0-py3-none-any.whl (4.6 kB)
Collecting transformer-smaller-training-vocab>=0.2.1 (from flair->textattack==0.3.8)
  Downloading transformer_smaller_training_vocab-0.2.4-py3-none-any.whl (13 kB)
Collecting beautifulsoup4 (from gdown==4.4.0->flair->textattack==0.3.8)
  Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.0/143.0 kB 49.8 MB/s eta 0:00:00
Collecting mccabe<0.8.0,>=0.7.0 (from flake8->textattack==0.3.8)
  Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Collecting pycodestyle<2.11.0,>=2.10.0 (from flake8->textattack==0.3.8)
  Downloading pycodestyle-2.10.0-py2.py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.3/41.3 kB 12.9 MB/s eta 0:00:00
Collecting pyflakes<3.1.0,>=3.0.0 (from flake8->textattack==0.3.8)
  Downloading pyflakes-3.0.1-py2.py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 29.6 MB/s eta 0:00:00
Collecting docutils (from nbsphinx->textattack==0.3.8)
  Downloading docutils-0.20.1-py3-none-any.whl (572 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 572.7/572.7 kB 93.8 MB/s eta 0:00:00
Collecting nbconvert!=5.4 (from nbsphinx->textattack==0.3.8)
  Downloading nbconvert-7.4.0-py3-none-any.whl (285 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 285.9/285.9 kB 78.0 MB/s eta 0:00:00
Requirement already satisfied: traitlets>=5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbsphinx->textattack==0.3.8) (5.9.0)
Collecting nbformat (from nbsphinx->textattack==0.3.8)
  Downloading nbformat-5.9.0-py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.6/77.6 kB 29.8 MB/s eta 0:00:00
Collecting sphinx>=1.8 (from nbsphinx->textattack==0.3.8)
  Downloading sphinx-7.0.1-py3-none-any.whl (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 107.8 MB/s eta 0:00:00
Collecting joblib (from nltk->textattack==0.3.8)
  Downloading joblib-1.2.0-py3-none-any.whl (297 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 298.0/298.0 kB 74.0 MB/s eta 0:00:00
Collecting docopt>=0.6.2 (from num2words->textattack==0.3.8)
  Downloading docopt-0.6.2.tar.gz (25 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting anytree (from OpenHowNet->textattack==0.3.8)
  Downloading anytree-2.8.0-py2.py3-none-any.whl (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.7/41.7 kB 18.9 MB/s eta 0:00:00
Collecting iniconfig (from pytest->textattack==0.3.8)
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting pluggy<2.0,>=0.12 (from pytest->textattack==0.3.8)
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting exceptiongroup>=1.0.0rc8 (from pytest->textattack==0.3.8)
  Downloading exceptiongroup-1.1.1-py3-none-any.whl (14 kB)
Collecting tomli>=1.0.0 (from pytest->textattack==0.3.8)
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting execnet>=1.1 (from pytest-xdist->textattack==0.3.8)
  Downloading execnet-1.9.0-py2.py3-none-any.whl (39 kB)
Collecting commonmark>=0.8.1 (from recommonmark->textattack==0.3.8)
  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.1/51.1 kB 22.6 MB/s eta 0:00:00
Collecting livereload (from sphinx-autobuild->textattack==0.3.8)
  Downloading livereload-2.6.3-py2.py3-none-any.whl (24 kB)
Collecting colorama (from sphinx-autobuild->textattack==0.3.8)
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting markdown>=3.4 (from sphinx-markdown-tables->textattack==0.3.8)
  Downloading Markdown-3.4.3-py3-none-any.whl (93 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.9/93.9 kB 36.5 MB/s eta 0:00:00
Collecting sphinx>=1.8 (from nbsphinx->textattack==0.3.8)
  Downloading sphinx-6.2.1-py3-none-any.whl (3.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 110.3 MB/s eta 0:00:00
Collecting docutils (from nbsphinx->textattack==0.3.8)
  Downloading docutils-0.18.1-py2.py3-none-any.whl (570 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 570.0/570.0 kB 94.4 MB/s eta 0:00:00
Collecting sphinxcontrib-jquery<5,>=4 (from sphinx-rtd-theme->textattack==0.3.8)
  Downloading sphinxcontrib_jquery-4.1-py2.py3-none-any.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.1/121.1 kB 44.6 MB/s eta 0:00:00
Collecting emoji (from stanza->textattack==0.3.8)
  Downloading emoji-2.5.0.tar.gz (355 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 355.8/355.8 kB 86.2 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting tornado (from visdom->textattack==0.3.8)
  Downloading tornado-6.3.2-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (426 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 426.9/426.9 kB 43.3 MB/s eta 0:00:00
Collecting jsonpatch (from visdom->textattack==0.3.8)
  Downloading jsonpatch-1.32-py2.py3-none-any.whl (12 kB)
Collecting websocket-client (from visdom->textattack==0.3.8)
  Downloading websocket_client-1.5.2-py3-none-any.whl (56 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.6/56.6 kB 27.0 MB/s eta 0:00:00
Collecting pillow (from visdom->textattack==0.3.8)
  Downloading Pillow-9.5.0-cp38-cp38-manylinux_2_28_x86_64.whl (3.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 68.5 MB/s eta 0:00:00
Collecting GitPython!=3.1.29,>=1.0.0 (from wandb->textattack==0.3.8)
  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 184.3/184.3 kB 58.1 MB/s eta 0:00:00
Collecting psutil>=5.0.0 (from wandb->textattack==0.3.8)
  Downloading psutil-5.9.5-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 282.1/282.1 kB 72.0 MB/s eta 0:00:00
Collecting sentry-sdk>=1.0.0 (from wandb->textattack==0.3.8)
  Downloading sentry_sdk-1.25.1-py2.py3-none-any.whl (206 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 206.7/206.7 kB 63.8 MB/s eta 0:00:00
Collecting docker-pycreds>=0.4.0 (from wandb->textattack==0.3.8)
  Downloading docker_pycreds-0.4.0-py2.py3-none-any.whl (9.0 kB)
Collecting pathtools (from wandb->textattack==0.3.8)
  Downloading pathtools-0.1.2.tar.gz (11 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting setproctitle (from wandb->textattack==0.3.8)
  Downloading setproctitle-1.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (31 kB)
Collecting attrs>=17.3.0 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading attrs-23.1.0-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 27.1 MB/s eta 0:00:00
Collecting multidict<7.0,>=4.5 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading multidict-6.0.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.3/121.3 kB 43.4 MB/s eta 0:00:00
Collecting async-timeout<5.0,>=4.0.0a3 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading async_timeout-4.0.2-py3-none-any.whl (5.8 kB)
Collecting yarl<2.0,>=1.0 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading yarl-1.9.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (266 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 266.9/266.9 kB 71.9 MB/s eta 0:00:00
Collecting frozenlist>=1.1.1 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading frozenlist-1.3.3-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (161 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 161.3/161.3 kB 54.0 MB/s eta 0:00:00
Collecting aiosignal>=1.1.2 (from aiohttp->datasets==2.4.0->textattack==0.3.8)
  Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Collecting gitdb<5,>=4.0.1 (from GitPython!=3.1.29,>=1.0.0->wandb->textattack==0.3.8)
  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.7/62.7 kB 30.3 MB/s eta 0:00:00
Collecting future (from hyperopt>=0.2.7->flair->textattack==0.3.8)
  Downloading future-0.18.3.tar.gz (840 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 840.9/840.9 kB 73.2 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting cloudpickle (from hyperopt>=0.2.7->flair->textattack==0.3.8)
  Downloading cloudpickle-2.2.1-py3-none-any.whl (25 kB)
Collecting py4j (from hyperopt>=0.2.7->flair->textattack==0.3.8)
  Downloading py4j-0.10.9.7-py2.py3-none-any.whl (200 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200.5/200.5 kB 59.0 MB/s eta 0:00:00
Collecting importlib-metadata>=4.4 (from markdown>=3.4->sphinx-markdown-tables->textattack==0.3.8)
  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)
Collecting contourpy>=1.0.1 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading contourpy-1.0.7-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (300 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 300.0/300.0 kB 75.0 MB/s eta 0:00:00
Collecting cycler>=0.10 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting fonttools>=4.22.0 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading fonttools-4.39.4-py3-none-any.whl (1.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 77.1 MB/s eta 0:00:00
Collecting kiwisolver>=1.0.1 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading kiwisolver-1.4.4-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 78.2 MB/s eta 0:00:00
Collecting pyparsing>=2.3.1 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.3/98.3 kB 39.9 MB/s eta 0:00:00
Collecting importlib-resources>=3.2.0 (from matplotlib->bert-score>=0.3.5->textattack==0.3.8)
  Downloading importlib_resources-5.12.0-py3-none-any.whl (36 kB)
Collecting bleach (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading bleach-6.0.0-py3-none-any.whl (162 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 162.5/162.5 kB 57.3 MB/s eta 0:00:00
Collecting defusedxml (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Collecting jupyter-core>=4.7 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading jupyter_core-5.3.0-py3-none-any.whl (93 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.2/93.2 kB 38.3 MB/s eta 0:00:00
Collecting jupyterlab-pygments (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading jupyterlab_pygments-0.2.2-py2.py3-none-any.whl (21 kB)
Collecting markupsafe>=2.0 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Collecting mistune<3,>=2.0.3 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading mistune-2.0.5-py2.py3-none-any.whl (24 kB)
Collecting nbclient>=0.5.0 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading nbclient-0.8.0-py3-none-any.whl (73 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.1/73.1 kB 30.5 MB/s eta 0:00:00
Collecting pandocfilters>=1.4.1 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading pandocfilters-1.5.0-py2.py3-none-any.whl (8.7 kB)
Requirement already satisfied: pygments>=2.4.1 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert!=5.4->nbsphinx->textattack==0.3.8) (2.15.1)
Collecting tinycss2 (from nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading tinycss2-1.2.1-py3-none-any.whl (21 kB)
Collecting fastjsonschema (from nbformat->nbsphinx->textattack==0.3.8)
  Downloading fastjsonschema-2.17.1-py3-none-any.whl (23 kB)
Collecting jsonschema>=2.6 (from nbformat->nbsphinx->textattack==0.3.8)
  Downloading jsonschema-4.17.3-py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.4/90.4 kB 36.8 MB/s eta 0:00:00
Collecting idna<4,>=2.5 (from requests>=2.19.0->datasets==2.4.0->textattack==0.3.8)
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 27.4 MB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1 (from requests>=2.19.0->datasets==2.4.0->textattack==0.3.8)
  Downloading urllib3-2.0.3-py3-none-any.whl (123 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.6/123.6 kB 46.1 MB/s eta 0:00:00
Collecting certifi>=2017.4.17 (from requests>=2.19.0->datasets==2.4.0->textattack==0.3.8)
  Downloading certifi-2023.5.7-py3-none-any.whl (156 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.0/157.0 kB 48.8 MB/s eta 0:00:00
Collecting threadpoolctl>=2.0.0 (from scikit-learn->sentence_transformers==2.2.0->textattack==0.3.8)
  Downloading threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Collecting sphinxcontrib-applehelp (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_applehelp-1.0.4-py3-none-any.whl (120 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 120.6/120.6 kB 46.4 MB/s eta 0:00:00
Collecting sphinxcontrib-devhelp (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_devhelp-1.0.2-py2.py3-none-any.whl (84 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.7/84.7 kB 37.3 MB/s eta 0:00:00
Collecting sphinxcontrib-jsmath (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl (5.1 kB)
Collecting sphinxcontrib-htmlhelp>=2.0.0 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_htmlhelp-2.0.1-py3-none-any.whl (99 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.8/99.8 kB 41.3 MB/s eta 0:00:00
Collecting sphinxcontrib-serializinghtml>=1.1.5 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_serializinghtml-1.1.5-py2.py3-none-any.whl (94 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 94.0/94.0 kB 36.9 MB/s eta 0:00:00
Collecting sphinxcontrib-qthelp (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading sphinxcontrib_qthelp-1.0.3-py2.py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.6/90.6 kB 37.9 MB/s eta 0:00:00
Collecting snowballstemmer>=2.0 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading snowballstemmer-2.2.0-py2.py3-none-any.whl (93 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.0/93.0 kB 38.2 MB/s eta 0:00:00
Collecting babel>=2.9 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading Babel-2.12.1-py3-none-any.whl (10.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 79.2 MB/s eta 0:00:00
Collecting alabaster<0.8,>=0.7 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading alabaster-0.7.13-py3-none-any.whl (13 kB)
Collecting imagesize>=1.3 (from sphinx>=1.8->nbsphinx->textattack==0.3.8)
  Downloading imagesize-1.4.1-py2.py3-none-any.whl (8.8 kB)
Collecting google-auth<3,>=1.6.3 (from tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading google_auth-2.19.1-py2.py3-none-any.whl (181 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.3/181.3 kB 58.9 MB/s eta 0:00:00
Collecting google-auth-oauthlib<0.5,>=0.4.1 (from tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading google_auth_oauthlib-0.4.6-py2.py3-none-any.whl (18 kB)
Collecting tensorboard-data-server<0.7.0,>=0.6.0 (from tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading tensorboard_data_server-0.6.1-py3-none-manylinux2010_x86_64.whl (4.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 80.8 MB/s eta 0:00:00
Collecting tensorboard-plugin-wit>=1.6.0 (from tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading tensorboard_plugin_wit-1.8.1-py3-none-any.whl (781 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 781.3/781.3 kB 76.0 MB/s eta 0:00:00
Collecting werkzeug>=1.0.1 (from tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading Werkzeug-2.3.6-py3-none-any.whl (242 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 69.9 MB/s eta 0:00:00
Collecting botocore<1.30.0,>=1.29.150 (from boto3->flair->textattack==0.3.8)
  Downloading botocore-1.29.150-py3-none-any.whl (10.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.9/10.9 MB 79.6 MB/s eta 0:00:00
Collecting jmespath<2.0.0,>=0.7.1 (from boto3->flair->textattack==0.3.8)
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.7.0,>=0.6.0 (from boto3->flair->textattack==0.3.8)
  Downloading s3transfer-0.6.1-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.8/79.8 kB 32.7 MB/s eta 0:00:00
Requirement already satisfied: wcwidth>=0.2.5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ftfy->flair->textattack==0.3.8) (0.2.6)
Collecting jsonpointer>=1.9 (from jsonpatch->visdom->textattack==0.3.8)
  Downloading jsonpointer-2.3-py2.py3-none-any.whl (7.8 kB)
INFO: pip is looking at multiple versions of multiprocess to determine which version is compatible with other requirements. This could take a while.
Collecting multiprocess (from datasets==2.4.0->textattack==0.3.8)
  Downloading multiprocess-0.70.13-py38-none-any.whl (131 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 131.4/131.4 kB 45.8 MB/s eta 0:00:00
Collecting mpmath>=0.19 (from sympy->torch!=1.8,>=1.7.0->textattack==0.3.8)
  Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 95.7 MB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1 (from requests>=2.19.0->datasets==2.4.0->textattack==0.3.8)
  Downloading urllib3-1.26.16-py2.py3-none-any.whl (143 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.1/143.1 kB 49.9 MB/s eta 0:00:00
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->GitPython!=3.1.29,>=1.0.0->wandb->textattack==0.3.8)
  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)
Collecting cachetools<6.0,>=2.0.0 (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading cachetools-5.3.1-py3-none-any.whl (9.3 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading pyasn1_modules-0.3.0-py2.py3-none-any.whl (181 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.3/181.3 kB 63.2 MB/s eta 0:00:00
Collecting rsa<5,>=3.1.4 (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading rsa-4.9-py3-none-any.whl (34 kB)
Collecting requests-oauthlib>=0.7.0 (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
Collecting zipp>=0.5 (from importlib-metadata>=4.4->markdown>=3.4->sphinx-markdown-tables->textattack==0.3.8)
  Downloading zipp-3.15.0-py3-none-any.whl (6.8 kB)
Collecting pkgutil-resolve-name>=1.3.10 (from jsonschema>=2.6->nbformat->nbsphinx->textattack==0.3.8)
  Downloading pkgutil_resolve_name-1.3.10-py3-none-any.whl (4.7 kB)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 (from jsonschema>=2.6->nbformat->nbsphinx->textattack==0.3.8)
  Downloading pyrsistent-0.19.3-py3-none-any.whl (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 26.0 MB/s eta 0:00:00
Collecting platformdirs>=2.5 (from jupyter-core>=4.7->nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading platformdirs-3.5.1-py3-none-any.whl (15 kB)
Collecting jupyter-client>=6.1.12 (from nbclient>=0.5.0->nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading jupyter_client-8.2.0-py3-none-any.whl (103 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.2/103.2 kB 37.8 MB/s eta 0:00:00
Collecting accelerate>=0.20.2 (from transformers>=4.21.0->textattack==0.3.8)
  Downloading accelerate-0.20.3-py3-none-any.whl (227 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.6/227.6 kB 63.1 MB/s eta 0:00:00
Collecting soupsieve>1.2 (from beautifulsoup4->gdown==4.4.0->flair->textattack==0.3.8)
  Downloading soupsieve-2.4.1-py3-none-any.whl (36 kB)
Collecting webencodings (from bleach->nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting pyzmq>=23.0 (from jupyter-client>=6.1.12->nbclient>=0.5.0->nbconvert!=5.4->nbsphinx->textattack==0.3.8)
  Downloading pyzmq-25.1.0-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 79.1 MB/s eta 0:00:00
Collecting pyasn1<0.6.0,>=0.4.6 (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading pyasn1-0.5.0-py2.py3-none-any.whl (83 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.9/83.9 kB 34.3 MB/s eta 0:00:00
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.10,>=2.9->tensorflow==2.9.1->textattack==0.3.8)
  Downloading oauthlib-3.2.2-py3-none-any.whl (151 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.7/151.7 kB 53.3 MB/s eta 0:00:00
Building wheels for collected packages: black, pinyin, sentence_transformers, gdown, mpld3, jieba, pycld2, visdom, word2number, docopt, sqlitedict, untokenize, emoji, langdetect, pathtools, pptree, future, lit
  Building wheel for black (pyproject.toml): started
  Building wheel for black (pyproject.toml): finished with status 'done'
  Created wheel for black: filename=black-20.8b1-py3-none-any.whl size=124177 sha256=ef92e782bd3d2fd08f0bf1092d07c8393c0f5a0ec60d788bb5c1e956ce5fe2ab
  Stored in directory: /home/runner/.cache/pip/wheels/95/a4/59/10cd5378d52f92cdb45025f040e4686e10ae5217961c25fd66
  Building wheel for pinyin (setup.py): started
  Building wheel for pinyin (setup.py): finished with status 'done'
  Created wheel for pinyin: filename=pinyin-0.4.0-py3-none-any.whl size=3630476 sha256=cc366ca0e035d92aaa9f7b57d807a81ae09d7dbf1f758fa70848b52120e0bb30
  Stored in directory: /home/runner/.cache/pip/wheels/d1/2a/d9/9c0f787a4d55f9a9eca26d322eafbe083bab41cb9bffb2e6e8
  Building wheel for sentence_transformers (setup.py): started
  Building wheel for sentence_transformers (setup.py): finished with status 'done'
  Created wheel for sentence_transformers: filename=sentence_transformers-2.2.0-py3-none-any.whl size=120735 sha256=3687837846373c56b93dc23fafce364770c757d28787fcf3218a47926e63ee5a
  Stored in directory: /home/runner/.cache/pip/wheels/0c/b6/fb/2289a932c365293ad865fc1fe9d2db694d5584241c6d670874
  Building wheel for gdown (pyproject.toml): started
  Building wheel for gdown (pyproject.toml): finished with status 'done'
  Created wheel for gdown: filename=gdown-4.4.0-py3-none-any.whl size=14759 sha256=d61eb6b8635247f7ef0b82c9a730b87dac76139659c42bfc45513cb92138919d
  Stored in directory: /home/runner/.cache/pip/wheels/7b/7b/5d/656f46cd6889e4c93977be9586901d0adc1271b2d876c84c96
  Building wheel for mpld3 (setup.py): started
  Building wheel for mpld3 (setup.py): finished with status 'done'
  Created wheel for mpld3: filename=mpld3-0.3-py3-none-any.whl size=116685 sha256=ca02f8b5c946e16d26de282815aac2c6657e0a42c8a5240e0e86f0b1231a36a6
  Stored in directory: /home/runner/.cache/pip/wheels/3d/9f/9d/d806a20bd97bc7076d724fa3e69fa5be61836ba16b2ffa6126
  Building wheel for jieba (setup.py): started
  Building wheel for jieba (setup.py): finished with status 'done'
  Created wheel for jieba: filename=jieba-0.42.1-py3-none-any.whl size=19314458 sha256=f9bbd1b5ffff0bda6117b94b58714ca2fdbff17bae943349ace0a5cbc11ecbd8
  Stored in directory: /home/runner/.cache/pip/wheels/ca/38/d8/dfdfe73bec1d12026b30cb7ce8da650f3f0ea2cf155ea018ae
  Building wheel for pycld2 (setup.py): started
  Building wheel for pycld2 (setup.py): finished with status 'done'
  Created wheel for pycld2: filename=pycld2-0.41-cp38-cp38-linux_x86_64.whl size=9907697 sha256=9f43a038c42a0bff90766cb7df9989f5af424402735c0dcf2aa1dbff853ea968
  Stored in directory: /home/runner/.cache/pip/wheels/2b/3a/82/d990040cbe6c3527732e931e2925785e83fe9aaa5a11c313ca
  Building wheel for visdom (setup.py): started
  Building wheel for visdom (setup.py): finished with status 'done'
  Created wheel for visdom: filename=visdom-0.2.4-py3-none-any.whl size=1408196 sha256=3a06a8ec86bcb620586e1fa6df33cc500cd8100ab10a35987d6351706df12226
  Stored in directory: /home/runner/.cache/pip/wheels/fb/b1/fc/b05c2c1930a412f01bd07dacaeb5fd8cc4bcccf71c835b0281
  Building wheel for word2number (setup.py): started
  Building wheel for word2number (setup.py): finished with status 'done'
  Created wheel for word2number: filename=word2number-1.1-py3-none-any.whl size=5569 sha256=ba0687b2b0e0982e754e7fefaad7395005b1da1909e1d682db768291a1e5f300
  Stored in directory: /home/runner/.cache/pip/wheels/cb/f3/5a/d88198fdeb46781ddd7e7f2653061af83e7adb2a076d8886d6
  Building wheel for docopt (setup.py): started
  Building wheel for docopt (setup.py): finished with status 'done'
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13707 sha256=124d87abf298941b4dcd9e0b584d8e1ee29ea30d3b5acf7065c268eebdd98b72
  Stored in directory: /home/runner/.cache/pip/wheels/56/ea/58/ead137b087d9e326852a851351d1debf4ada529b6ac0ec4e8c
  Building wheel for sqlitedict (setup.py): started
  Building wheel for sqlitedict (setup.py): finished with status 'done'
  Created wheel for sqlitedict: filename=sqlitedict-2.1.0-py3-none-any.whl size=16863 sha256=2dff1ecc7a00b0dadc4f731e9d3a508f820d3b2e91827dd3956e35ded65efd2c
  Stored in directory: /home/runner/.cache/pip/wheels/04/c6/16/46e174009277f9bccdaa7215a243939d2f70180804b249bf3a
  Building wheel for untokenize (setup.py): started
  Building wheel for untokenize (setup.py): finished with status 'done'
  Created wheel for untokenize: filename=untokenize-0.1.1-py3-none-any.whl size=2874 sha256=65b40e466fb25b27b637f02a45e5498440907615c046ca8965e0b95829880f76
  Stored in directory: /home/runner/.cache/pip/wheels/04/b2/49/dcd5c8338e970f80d601fea7e2e1878c05df409ae374d6d91a
  Building wheel for emoji (setup.py): started
  Building wheel for emoji (setup.py): finished with status 'done'
  Created wheel for emoji: filename=emoji-2.5.0-py2.py3-none-any.whl size=351211 sha256=5baa4c98b95f528bd269f3624ef1192b820c9467b94dd42e630203843a21b7e4
  Stored in directory: /home/runner/.cache/pip/wheels/da/49/24/cb21796af9cb51e5345c67794f4e2e15800a77a31722e2aa47
  Building wheel for langdetect (setup.py): started
  Building wheel for langdetect (setup.py): finished with status 'done'
  Created wheel for langdetect: filename=langdetect-1.0.9-py3-none-any.whl size=993224 sha256=95aa065541c79c121437fb3d90ce3a9c79d9a8fe7ba1d2b5d096cd9071107670
  Stored in directory: /home/runner/.cache/pip/wheels/13/c7/b0/79f66658626032e78fc1a83103690ef6797d551cb22e56e734
  Building wheel for pathtools (setup.py): started
  Building wheel for pathtools (setup.py): finished with status 'done'
  Created wheel for pathtools: filename=pathtools-0.1.2-py3-none-any.whl size=8791 sha256=fe955d86698b9b6fc9da070ea27894b4e9bf3a346c3ec4f7bead1ba447d4a2b1
  Stored in directory: /home/runner/.cache/pip/wheels/4c/8e/7e/72fbc243e1aeecae64a96875432e70d4e92f3d2d18123be004
  Building wheel for pptree (setup.py): started
  Building wheel for pptree (setup.py): finished with status 'done'
  Created wheel for pptree: filename=pptree-3.1-py3-none-any.whl size=4609 sha256=8f11ab7b9cb97a6e29651330140687f6810fb5d3c68f90eaec7ac599ecd7e903
  Stored in directory: /home/runner/.cache/pip/wheels/e1/8b/30/5b20240d3d13a9dfafb6a6dd49d1b541c86d39812cb3690edf
  Building wheel for future (setup.py): started
  Building wheel for future (setup.py): finished with status 'done'
  Created wheel for future: filename=future-0.18.3-py3-none-any.whl size=492022 sha256=9688f33101dff69ffd46122f39bf37c01049b533b0bfcdd699513974d54803c2
  Stored in directory: /home/runner/.cache/pip/wheels/a0/0b/ee/e6994fadb42c1354dcccb139b0bf2795271bddfe6253ccdf11
  Building wheel for lit (setup.py): started
  Building wheel for lit (setup.py): finished with status 'done'
  Created wheel for lit: filename=lit-16.0.5.post0-py3-none-any.whl size=88257 sha256=c2b935fa5fd5e6f3894944e07cfd3a007b06b1938c51b580e0bd5314732350f8
  Stored in directory: /home/runner/.cache/pip/wheels/8f/1f/ae/dac02ad52cca765f5f75b090964a3e71db5a2bc327fff49d0e
Successfully built black pinyin sentence_transformers gdown mpld3 jieba pycld2 visdom word2number docopt sqlitedict untokenize emoji langdetect pathtools pptree future lit
Installing collected packages: word2number, webencodings, untokenize, tokenizers, tensorboard-plugin-wit, sqlitedict, snowballstemmer, sentencepiece, safetensors, pytz, pycld2, py4j, pptree, pinyin, pathtools, mpmath, mpld3, mistune, lru-dict, lit, libclang, keras, jieba, janome, flatbuffers, fastjsonschema, docopt, commonmark, cmake, appdirs, zipp, xxhash, wrapt, websocket-client, urllib3, tzdata, typed-ast, tqdm, tornado, tomli, toml, tinycss2, threadpoolctl, terminaltables, termcolor, tensorflow-io-gcs-filesystem, tensorflow-estimator, tensorboard-data-server, tabulate, sympy, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, soupsieve, smmap, smart-open, setproctitle, regex, pyzmq, pyyaml, python-dateutil, PySocks, pyrsistent, pyparsing, pyflakes, pycodestyle, pyasn1, psutil, protobuf, pluggy, platformdirs, pkgutil-resolve-name, pillow, pathspec, pandocfilters, packaging, oauthlib, nvidia-nvtx-cu11, nvidia-nccl-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cufft-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-cupti-cu11, nvidia-cublas-cu11, numpy, num2words, networkx, mypy-extensions, multidict, more-itertools, mccabe, markupsafe, lxml, langdetect, kiwisolver, jupyterlab-pygments, jsonpointer, joblib, jmespath, isort, iniconfig, imagesize, idna, grpcio, google-pasta, gast, future, ftfy, fsspec, frozenlist, fonttools, filelock, execnet, exceptiongroup, emoji, editdistance, docutils, docker-pycreds, dill, defusedxml, cycler, conllu, colorama, cloudpickle, click, charset_normalizer, certifi, cachetools, bleach, babel, attrs, async-timeout, astunparse, anytree, alabaster, absl-py, yarl, werkzeug, tensorflow_hub, tensorboardX, sentry-sdk, segtok, scipy, rsa, requests, pytest, pyasn1-modules, pyarrow, pandas, opt-einsum, nvidia-cusolver-cu11, nvidia-cudnn-cu11, nltk, multiprocess, livereload, lemminflect, keras-preprocessing, jupyter-core, jsonpatch, jinja2, importlib-resources, importlib-metadata, h5py, gitdb, flake8, docformatter, deprecated, contourpy, botocore, black, beautifulsoup4, aiosignal, wikipedia-api, visdom, sphinx, scikit-learn, s3transfer, responses, requests-oauthlib, pytest-xdist, OpenHowNet, matplotlib, markdown, language_tool_python, jupyter-client, jsonschema, hyperopt, huggingface-hub, google-auth, GitPython, gensim, aiohttp, wandb, transformers, sphinxcontrib-jquery, sphinx-markdown-tables, sphinx-copybutton, sphinx-autobuild, recommonmark, nbformat, google-auth-oauthlib, gdown, bpemb, boto3, tensorboard, sphinx-rtd-theme, nbclient, datasets, tensorflow, nbconvert, tensorflow_text, nbsphinx, triton, torch, accelerate, transformer-smaller-training-vocab, pytorch-revgrad, torchvision, flair, bert-score, textattack, stanza, sentence_transformers
  Attempting uninstall: textattack
    Found existing installation: textattack 0.3.8
    Uninstalling textattack-0.3.8:
      Successfully uninstalled textattack-0.3.8
  Running setup.py develop for textattack
Successfully installed GitPython-3.1.31 OpenHowNet-2.0 PySocks-1.7.1 absl-py-1.4.0 accelerate-0.20.3 aiohttp-3.8.4 aiosignal-1.3.1 alabaster-0.7.13 anytree-2.8.0 appdirs-1.4.4 astunparse-1.6.3 async-timeout-4.0.2 attrs-23.1.0 babel-2.12.1 beautifulsoup4-4.12.2 bert-score-0.3.13 black-20.8b1 bleach-6.0.0 boto3-1.26.150 botocore-1.29.150 bpemb-0.3.4 cachetools-5.3.1 certifi-2023.5.7 charset_normalizer-3.1.0 click-8.0.4 cloudpickle-2.2.1 cmake-3.26.4 colorama-0.4.6 commonmark-0.9.1 conllu-4.5.2 contourpy-1.0.7 cycler-0.11.0 datasets-2.4.0 defusedxml-0.7.1 deprecated-1.2.14 dill-0.3.5.1 docformatter-1.7.2 docker-pycreds-0.4.0 docopt-0.6.2 docutils-0.18.1 editdistance-0.6.2 emoji-2.5.0 exceptiongroup-1.1.1 execnet-1.9.0 fastjsonschema-2.17.1 filelock-3.12.0 flair-0.12.2 flake8-6.0.0 flatbuffers-1.12 fonttools-4.39.4 frozenlist-1.3.3 fsspec-2023.5.0 ftfy-6.1.1 future-0.18.3 gast-0.4.0 gdown-4.4.0 gensim-4.1.2 gitdb-4.0.10 google-auth-2.19.1 google-auth-oauthlib-0.4.6 google-pasta-0.2.0 grpcio-1.54.2 h5py-3.8.0 huggingface-hub-0.15.1 hyperopt-0.2.7 idna-3.4 imagesize-1.4.1 importlib-metadata-6.6.0 importlib-resources-5.12.0 iniconfig-2.0.0 isort-5.6.4 janome-0.4.2 jieba-0.42.1 jinja2-3.1.2 jmespath-1.0.1 joblib-1.2.0 jsonpatch-1.32 jsonpointer-2.3 jsonschema-4.17.3 jupyter-client-8.2.0 jupyter-core-5.3.0 jupyterlab-pygments-0.2.2 keras-2.9.0 keras-preprocessing-1.1.2 kiwisolver-1.4.4 langdetect-1.0.9 language_tool_python-2.7.1 lemminflect-0.2.3 libclang-16.0.0 lit-16.0.5.post0 livereload-2.6.3 lru-dict-1.2.0 lxml-4.9.2 markdown-3.4.3 markupsafe-2.1.3 matplotlib-3.7.1 mccabe-0.7.0 mistune-2.0.5 more-itertools-9.1.0 mpld3-0.3 mpmath-1.3.0 multidict-6.0.4 multiprocess-0.70.13 mypy-extensions-1.0.0 nbclient-0.8.0 nbconvert-7.4.0 nbformat-5.9.0 nbsphinx-0.9.2 networkx-3.1 nltk-3.8.1 num2words-0.5.12 numpy-1.24.3 nvidia-cublas-cu11-11.10.3.66 nvidia-cuda-cupti-cu11-11.7.101 nvidia-cuda-nvrtc-cu11-11.7.99 nvidia-cuda-runtime-cu11-11.7.99 nvidia-cudnn-cu11-8.5.0.96 nvidia-cufft-cu11-10.9.0.58 nvidia-curand-cu11-10.2.10.91 nvidia-cusolver-cu11-11.4.0.1 nvidia-cusparse-cu11-11.7.4.91 nvidia-nccl-cu11-2.14.3 nvidia-nvtx-cu11-11.7.91 oauthlib-3.2.2 opt-einsum-3.3.0 packaging-23.1 pandas-2.0.2 pandocfilters-1.5.0 pathspec-0.11.1 pathtools-0.1.2 pillow-9.5.0 pinyin-0.4.0 pkgutil-resolve-name-1.3.10 platformdirs-3.5.1 pluggy-1.0.0 pptree-3.1 protobuf-3.19.6 psutil-5.9.5 py4j-0.10.9.7 pyarrow-12.0.0 pyasn1-0.5.0 pyasn1-modules-0.3.0 pycld2-0.41 pycodestyle-2.10.0 pyflakes-3.0.1 pyparsing-3.0.9 pyrsistent-0.19.3 pytest-7.3.1 pytest-xdist-3.3.1 python-dateutil-2.8.2 pytorch-revgrad-0.2.0 pytz-2023.3 pyyaml-6.0 pyzmq-25.1.0 recommonmark-0.7.1 regex-2023.6.3 requests-2.31.0 requests-oauthlib-1.3.1 responses-0.18.0 rsa-4.9 s3transfer-0.6.1 safetensors-0.3.1 scikit-learn-1.2.2 scipy-1.10.1 segtok-1.5.11 sentence_transformers-2.2.0 sentencepiece-0.1.99 sentry-sdk-1.25.1 setproctitle-1.3.2 smart-open-6.3.0 smmap-5.0.0 snowballstemmer-2.2.0 soupsieve-2.4.1 sphinx-6.2.1 sphinx-autobuild-2021.3.14 sphinx-copybutton-0.5.2 sphinx-markdown-tables-0.0.17 sphinx-rtd-theme-1.2.2 sphinxcontrib-applehelp-1.0.4 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.1 sphinxcontrib-jquery-4.1 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 sqlitedict-2.1.0 stanza-1.5.0 sympy-1.12 tabulate-0.9.0 tensorboard-2.9.1 tensorboard-data-server-0.6.1 tensorboard-plugin-wit-1.8.1 tensorboardX-2.6 tensorflow-2.9.1 tensorflow-estimator-2.9.0 tensorflow-io-gcs-filesystem-0.32.0 tensorflow_hub-0.13.0 tensorflow_text-2.9.0 termcolor-2.3.0 terminaltables-3.1.10 textattack-0.3.8 threadpoolctl-3.1.0 tinycss2-1.2.1 tokenizers-0.13.3 toml-0.10.2 tomli-2.0.1 torch-2.0.1 torchvision-0.15.2 tornado-6.3.2 tqdm-4.65.0 transformer-smaller-training-vocab-0.2.4 transformers-4.30.0 triton-2.0.0 typed-ast-1.5.4 tzdata-2023.3 untokenize-0.1.1 urllib3-1.26.16 visdom-0.2.4 wandb-0.15.4 webencodings-0.5.1 websocket-client-1.5.2 werkzeug-2.3.6 wikipedia-api-0.5.8 word2number-1.1 wrapt-1.15.0 xxhash-3.2.0 yarl-1.9.2 zipp-3.15.0
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting ipykernel<5.0.0
  Downloading ipykernel-4.10.1-py3-none-any.whl (109 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.9/109.9 kB 3.4 MB/s eta 0:00:00
Collecting ipython<7.0.0
  Downloading ipython-6.5.0-py3-none-any.whl (748 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 748.4/748.4 kB 8.9 MB/s eta 0:00:00
Collecting notebook (from jupyter)
  Downloading notebook-6.5.4-py3-none-any.whl (529 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 529.8/529.8 kB 12.9 MB/s eta 0:00:00
Collecting qtconsole (from jupyter)
  Downloading qtconsole-5.4.3-py3-none-any.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.9/121.9 kB 12.6 MB/s eta 0:00:00
Collecting jupyter-console (from jupyter)
  Downloading jupyter_console-6.6.3-py3-none-any.whl (24 kB)
Requirement already satisfied: nbconvert in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter) (7.4.0)
Collecting ipywidgets (from jupyter)
  Downloading ipywidgets-8.0.6-py3-none-any.whl (138 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 138.3/138.3 kB 14.2 MB/s eta 0:00:00
Requirement already satisfied: traitlets>=4.1.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipykernel<5.0.0) (5.9.0)
Requirement already satisfied: jupyter-client in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipykernel<5.0.0) (8.2.0)
Requirement already satisfied: tornado>=4.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipykernel<5.0.0) (6.3.2)
Requirement already satisfied: setuptools>=18.5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (67.8.0)
Requirement already satisfied: jedi>=0.10 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (0.18.2)
Requirement already satisfied: decorator in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (5.1.1)
Requirement already satisfied: pickleshare in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (0.7.5)
Collecting simplegeneric>0.8 (from ipython<7.0.0)
  Downloading simplegeneric-0.8.1.zip (12 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting prompt-toolkit<2.0.0,>=1.0.15 (from ipython<7.0.0)
  Downloading prompt_toolkit-1.0.18-py3-none-any.whl (245 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 245.4/245.4 kB 19.3 MB/s eta 0:00:00
Requirement already satisfied: pygments in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (2.15.1)
Requirement already satisfied: backcall in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (0.2.0)
Requirement already satisfied: pexpect in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from ipython<7.0.0) (4.8.0)
Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jedi>=0.10->ipython<7.0.0) (0.8.3)
Requirement already satisfied: six>=1.9.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from prompt-toolkit<2.0.0,>=1.0.15->ipython<7.0.0) (1.16.0)
Requirement already satisfied: wcwidth in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from prompt-toolkit<2.0.0,>=1.0.15->ipython<7.0.0) (0.2.6)
Collecting widgetsnbextension~=4.0.7 (from ipywidgets->jupyter)
  Downloading widgetsnbextension-4.0.7-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 23.0 MB/s eta 0:00:00
Collecting jupyterlab-widgets~=3.0.7 (from ipywidgets->jupyter)
  Downloading jupyterlab_widgets-3.0.7-py3-none-any.whl (198 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 198.2/198.2 kB 37.7 MB/s eta 0:00:00
Requirement already satisfied: importlib-metadata>=4.8.3 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-client->ipykernel<5.0.0) (6.6.0)
Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-client->ipykernel<5.0.0) (5.3.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-client->ipykernel<5.0.0) (2.8.2)
Requirement already satisfied: pyzmq>=23.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-client->ipykernel<5.0.0) (25.1.0)
INFO: pip is looking at multiple versions of jupyter-console to determine which version is compatible with other requirements. This could take a while.
Collecting jupyter-console (from jupyter)
  Downloading jupyter_console-6.6.2-py3-none-any.whl (24 kB)
  Downloading jupyter_console-6.6.1-py3-none-any.whl (24 kB)
  Downloading jupyter_console-6.6.0-py3-none-any.whl (24 kB)
  Downloading jupyter_console-6.5.1-py3-none-any.whl (23 kB)
  Downloading jupyter_console-6.5.0-py3-none-any.whl (23 kB)
  Downloading jupyter_console-6.4.4-py3-none-any.whl (22 kB)
  Downloading jupyter_console-6.4.3-py3-none-any.whl (22 kB)
INFO: pip is looking at multiple versions of jupyter-console to determine which version is compatible with other requirements. This could take a while.
  Downloading jupyter_console-6.4.2-py3-none-any.whl (23 kB)
  Downloading jupyter_console-6.4.1-py3-none-any.whl (23 kB)
  Downloading jupyter_console-6.4.0-py3-none-any.whl (22 kB)
  Downloading jupyter_console-6.3.0-py3-none-any.whl (22 kB)
  Downloading jupyter_console-6.2.0-py3-none-any.whl (22 kB)
INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.
  Downloading jupyter_console-6.1.0-py2.py3-none-any.whl (21 kB)
  Downloading jupyter_console-6.0.0-py2.py3-none-any.whl (21 kB)
  Downloading jupyter_console-5.2.0-py2.py3-none-any.whl (20 kB)
Requirement already satisfied: beautifulsoup4 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (4.12.2)
Requirement already satisfied: bleach in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (6.0.0)
Requirement already satisfied: defusedxml in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (0.7.1)
Requirement already satisfied: jinja2>=3.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (3.1.2)
Requirement already satisfied: jupyterlab-pygments in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (0.2.2)
Requirement already satisfied: markupsafe>=2.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (2.1.3)
Requirement already satisfied: mistune<3,>=2.0.3 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (2.0.5)
Requirement already satisfied: nbclient>=0.5.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (0.8.0)
Requirement already satisfied: nbformat>=5.1 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (5.9.0)
Requirement already satisfied: packaging in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (23.1)
Requirement already satisfied: pandocfilters>=1.4.1 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (1.5.0)
Requirement already satisfied: tinycss2 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbconvert->jupyter) (1.2.1)
Collecting argon2-cffi (from notebook->jupyter)
  Downloading argon2_cffi-21.3.0-py3-none-any.whl (14 kB)
Collecting ipython-genutils (from notebook->jupyter)
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting nest-asyncio>=1.5 (from notebook->jupyter)
  Downloading nest_asyncio-1.5.6-py3-none-any.whl (5.2 kB)
Collecting Send2Trash>=1.8.0 (from notebook->jupyter)
  Downloading Send2Trash-1.8.2-py3-none-any.whl (18 kB)
Collecting terminado>=0.8.3 (from notebook->jupyter)
  Downloading terminado-0.17.1-py3-none-any.whl (17 kB)
Collecting prometheus-client (from notebook->jupyter)
  Downloading prometheus_client-0.17.0-py3-none-any.whl (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.6/60.6 kB 27.2 MB/s eta 0:00:00
Collecting nbclassic>=0.4.7 (from notebook->jupyter)
  Downloading nbclassic-1.0.0-py3-none-any.whl (10.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.0/10.0 MB 50.3 MB/s eta 0:00:00
Requirement already satisfied: ptyprocess>=0.5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from pexpect->ipython<7.0.0) (0.7.0)
Collecting qtpy>=2.0.1 (from qtconsole->jupyter)
  Downloading QtPy-2.3.1-py3-none-any.whl (84 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.9/84.9 kB 34.0 MB/s eta 0:00:00
Requirement already satisfied: zipp>=0.5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from importlib-metadata>=4.8.3->jupyter-client->ipykernel<5.0.0) (3.15.0)
Requirement already satisfied: platformdirs>=2.5 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-core!=5.0.*,>=4.12->jupyter-client->ipykernel<5.0.0) (3.5.1)
Collecting jupyter-server>=1.8 (from nbclassic>=0.4.7->notebook->jupyter)
  Downloading jupyter_server-2.6.0-py3-none-any.whl (375 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 375.0/375.0 kB 78.5 MB/s eta 0:00:00
Collecting notebook-shim>=0.2.3 (from nbclassic>=0.4.7->notebook->jupyter)
  Downloading notebook_shim-0.2.3-py3-none-any.whl (13 kB)
Requirement already satisfied: fastjsonschema in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbformat>=5.1->nbconvert->jupyter) (2.17.1)
Requirement already satisfied: jsonschema>=2.6 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from nbformat>=5.1->nbconvert->jupyter) (4.17.3)
Collecting argon2-cffi-bindings (from argon2-cffi->notebook->jupyter)
  Downloading argon2_cffi_bindings-21.2.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (86 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.2/86.2 kB 36.4 MB/s eta 0:00:00
Requirement already satisfied: soupsieve>1.2 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from beautifulsoup4->nbconvert->jupyter) (2.4.1)
Requirement already satisfied: webencodings in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from bleach->nbconvert->jupyter) (0.5.1)
Requirement already satisfied: attrs>=17.4.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter) (23.1.0)
Requirement already satisfied: importlib-resources>=1.4.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter) (5.12.0)
Requirement already satisfied: pkgutil-resolve-name>=1.3.10 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter) (1.3.10)
Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter) (0.19.3)
Collecting anyio>=3.1.0 (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading anyio-3.7.0-py3-none-any.whl (80 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.9/80.9 kB 31.0 MB/s eta 0:00:00
Collecting jupyter-events>=0.6.0 (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading jupyter_events-0.6.3-py3-none-any.whl (18 kB)
Collecting jupyter-server-terminals (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading jupyter_server_terminals-0.4.4-py3-none-any.whl (13 kB)
Collecting overrides (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading overrides-7.3.1-py3-none-any.whl (17 kB)
Requirement already satisfied: websocket-client in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter) (1.5.2)
Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi->notebook->jupyter)
  Downloading cffi-1.15.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (442 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 442.7/442.7 kB 87.6 MB/s eta 0:00:00
Requirement already satisfied: idna>=2.8 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from anyio>=3.1.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter) (3.4)
Collecting sniffio>=1.1 (from anyio>=3.1.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)
Requirement already satisfied: exceptiongroup in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from anyio>=3.1.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter) (1.1.1)
Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook->jupyter)
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 45.3 MB/s eta 0:00:00
Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.6.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading python_json_logger-2.0.7-py3-none-any.whl (8.1 kB)
Requirement already satisfied: pyyaml>=5.3 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jupyter-events>=0.6.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter) (6.0)
Collecting rfc3339-validator (from jupyter-events>=0.6.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.6.0->jupyter-server>=1.8->nbclassic>=0.4.7->notebook->jupyter)
  Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
Collecting fqdn (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter)
  Downloading fqdn-1.5.1-py3-none-any.whl (9.1 kB)
Collecting isoduration (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter)
  Downloading isoduration-20.11.0-py3-none-any.whl (11 kB)
Requirement already satisfied: jsonpointer>1.13 in /opt/hostedtoolcache/Python/3.8.16/x64/lib/python3.8/site-packages (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter) (2.3)
Collecting uri-template (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter)
  Downloading uri_template-1.2.0-py3-none-any.whl (10 kB)
Collecting webcolors>=1.11 (from jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter)
  Downloading webcolors-1.13-py3-none-any.whl (14 kB)
Collecting arrow>=0.15.0 (from isoduration->jsonschema>=2.6->nbformat>=5.1->nbconvert->jupyter)
  Downloading arrow-1.2.3-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.4/66.4 kB 27.8 MB/s eta 0:00:00
Building wheels for collected packages: simplegeneric
  Building wheel for simplegeneric (setup.py): started
  Building wheel for simplegeneric (setup.py): finished with status 'done'
  Created wheel for simplegeneric: filename=simplegeneric-0.8.1-py3-none-any.whl size=5059 sha256=a4e7cb2a141dfabce49607d94bb861572c5c5e60c0236244fae747c08eb0cd5a
  Stored in directory: /home/runner/.cache/pip/wheels/0b/32/6b/5f5447909a062da20dfe432fa945d8f98636692637deccaa8a
Successfully built simplegeneric
Installing collected packages: simplegeneric, ipython-genutils, widgetsnbextension, webcolors, uri-template, terminado, sniffio, Send2Trash, rfc3986-validator, rfc3339-validator, qtpy, python-json-logger, pycparser, prompt-toolkit, prometheus-client, overrides, nest-asyncio, jupyterlab-widgets, fqdn, jupyter-server-terminals, ipython, cffi, arrow, anyio, isoduration, ipykernel, argon2-cffi-bindings, qtconsole, jupyter-console, ipywidgets, argon2-cffi, jupyter-events, jupyter-server, notebook-shim, nbclassic, notebook, jupyter
  Attempting uninstall: prompt-toolkit
    Found existing installation: prompt-toolkit 3.0.38
    Uninstalling prompt-toolkit-3.0.38:
      Successfully uninstalled prompt-toolkit-3.0.38
  Attempting uninstall: ipython
    Found existing installation: ipython 8.12.2
    Uninstalling ipython-8.12.2:
      Successfully uninstalled ipython-8.12.2
Successfully installed Send2Trash-1.8.2 anyio-3.7.0 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 arrow-1.2.3 cffi-1.15.1 fqdn-1.5.1 ipykernel-4.10.1 ipython-6.5.0 ipython-genutils-0.2.0 ipywidgets-8.0.6 isoduration-20.11.0 jupyter-1.0.0 jupyter-console-5.2.0 jupyter-events-0.6.3 jupyter-server-2.6.0 jupyter-server-terminals-0.4.4 jupyterlab-widgets-3.0.7 nbclassic-1.0.0 nest-asyncio-1.5.6 notebook-6.5.4 notebook-shim-0.2.3 overrides-7.3.1 prometheus-client-0.17.0 prompt-toolkit-1.0.18 pycparser-2.21 python-json-logger-2.0.7 qtconsole-5.4.3 qtpy-2.3.1 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 simplegeneric-0.8.1 sniffio-1.3.0 terminado-0.17.1 uri-template-1.2.0 webcolors-1.13 widgetsnbextension-4.0.7
2m 21s
0s
0s
