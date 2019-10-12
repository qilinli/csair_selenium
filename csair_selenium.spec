# -*- mode: python -*-

block_cipher = None


a = Analysis(['csair_selenium.py'],
             pathex=['/Users/qilin/research/spider/ctrip_selenium'],
             binaries=[('/usr/local/bin/chromedriver', '.')],
             datas=[('/Users/qilin/research/spider/ctrip_selenium/dates.txt', '.'), ('/Users/qilin/research/spider/ctrip_selenium/prices.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='csair_selenium',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='csair_selenium')