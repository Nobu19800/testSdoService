#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import sys

import OpenRTM_aist
import RTC, RTC__POA
import OpenRTM, OpenRTM__POA

testcomp_spec = ["implementation_id", "TestComp",
                 "type_name",         "TestComp",
                 "description",       "Test example component",
                 "version",           "1.0",
                 "vendor",            "Nobuhiko Myiyamoto",
                 "category",          "example",
                 "activity_type",     "DataFlowComponent",
                 "max_instance",      "10",
                 "language",          "C++",
                 "lang_type",         "compile",
                 ""]


class TestComp(OpenRTM_aist.DataFlowComponentBase):
  def __init__(self, manager):
    OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
  def onInitialize(self):
    return RTC.RTC_OK

def TestCompInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=testcomp_spec)
    manager.registerFactory(profile,
                            TestComp,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    TestCompInit(manager)
    comp = manager.createComponent("TestComp")

def main():
  mgr = OpenRTM_aist.Manager.init(sys.argv)
  mgr.setModuleInitProc(MyModuleInit)
  mgr.activateManager()
  mgr.runManager()


if __name__ == "__main__":
	main()