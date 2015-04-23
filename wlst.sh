#!/bin/bash

export JAVA_HOME=/opt/java/current

PATH=$JAVA_HOME/bin:$PATH

export WL_HOME=/opt/Oracle/Middleware/wlserver_12.1
export CLASSPATH=.:$WL_HOME/server/lib/weblogic.jar

java weblogic.WLST $@


