# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import collect_all

fitz_datas, fitz_binaries, fitz_hiddenimports = collect_all('fitz')


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=fitz_binaries,
    datas=[
        ('config.json', '.')
    ] + fitz_datas,
    hiddenimports=[
        'fitz',
        'frontend',
        'gui',
        'pdf_processor'
    ] + fitz_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)


pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)


exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='EtiquetaA5',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)