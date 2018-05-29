#!/usr/bin/sh
#Shell script to check if the process is not running and start it again

check_process(){
        # check the args
        if [ "$1" = "" ];
        then
                return 0
        fi

        #PROCESS_NUM => get the process number regarding the given thread name
        PROCESS_NUM=$(ps -ef | grep "$1" | grep -v "grep" | wc -l)
        # for degbuging...
        echo $(ps -ef | grep "$1" | grep -v "grep")
        if [ $PROCESS_NUM -eq 1 ];
        then
                return 1
        else
                return 0
        fi
}

# check wheter the instance of thread exsits
while [ 1 ] ; do
        echo 'begin checking...'
        check_process "python collect_urls_guardian.py" # the thread name
        CHECK_RET=$?
        if [ $CHECK_RET -eq 0 ]; # none exist
        then
                # do something...
				echo "Python process is not running starting it now"
				 nohup /usr/bin/python2.7 collect_urls_guardian.py &
        else
				echo "Python process is still running"
		fi
        sleep 30
done
