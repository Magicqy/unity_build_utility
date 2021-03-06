#!/usr/bin/python
import sys, os, time
import buildutil as utl

start = time.time()

UNITY_PROJ = './TestProject'
BUILD_PATH = os.path.join(UNITY_PROJ, 'Builds')
EXPORT_PROJ = os.path.join(BUILD_PATH, 'ios-proj')
OUT_FILE = os.path.join(BUILD_PATH, 'ios-output.ipa')

BUNDLE_ID = 'com.test.proj'
PROV_FILE = 'MOBILE_PROVISION_FILE_PATH'
KEY_CHAIN = ['CODE_SIGN_KEY_CHAIN_FILE_PATH', 'CODE_SIGN_KEY_CHAIN_PASSWORD}']

shared_args = dict(
    # unityHome = 'UNITY_HOME_PATH',
    unityLog = os.path.join(BUILD_PATH, 'unity.log'),
    log = os.path.join(BUILD_PATH, 'build.log'),
)

utl.runTask(utl.INVOKE, shared_args,
    projPath = UNITY_PROJ,
    calls = [['UnityEditor.PlayerSettings.bundleIdentifier', BUNDLE_ID]])

utl.runTask(utl.BUILD, shared_args,
    projPath = UNITY_PROJ,
    buildTarget = 'ios',
    outPath = EXPORT_PROJ)
    
utl.runTask(utl.PACK_IOS, shared_args,
    projPath = EXPORT_PROJ,
    outFile = OUT_FILE,
    provFile = PROV_FILE,
    keychain = KEY_CHAIN)

print('===time passed===')
print(time.time()-start)