#! /bin/bash
echo "HostName: `hostname`"
echo "Sniper working directory: /path/to/sniper/benchmarks"
if [ -f "app.source" ]; then
source app.source
fi
export RUN_DIR=/path/to/sniper 
export SNIPER_DIR=${RUN_DIR}/benchmarks
if [ -z "${APP_BINARY}" ]; then				#to check whether a string is empty
echo "[Warning] Environment variable APP_BINARY is not set"
export APP_BINARY=parsec-swaptions
else
echo "Environment variable set for APP_BINARY:${APP_BINARY}"
fi
if [ -z "${APP_OPTS}" ]; then
echo "[Warning] Environment variable APP_OPTS is not set"
export APP_OPTS="cmd_options_file.txt"
else
echo "Environment variable set for APP_OPTS:${APP_OPTS}"
fi
echo "Application binary: ${APP_BINARY}"
echo "Application options: ${APP_OPTS}"

binary=${APP_BINARY}
commandline_option=${APP_OPTS}
if [ -f "cmd_options_file.txt" ]; then
commandline_option=`cat cmd_options_file.txt`
fi

$SNIPER_DIR/run-sniper --benchmarks=${binary}-test-1 \
                        -n 4 \
                        -c cortex.cfg \
			-g --perf_model/core/interval_timer/window_size=${window_size} \
                        -g --perf_model/core/interval_timer/dispatch_width=${dispatch_width} \
			-g --perf_model/l1_icache/cache_size=${l1i_size} \
			-g --perf_model/l1_icache/associativity=${l1i_associativity} \
			-g --perf_model/l1_dcache/cache_size=${l1d_size} \
			-g --perf_model/l1_dcache/associativity=${l1d_associativity} \
			-g --perf_model/l2_cache/cache_size=${l2_size} \
			-g --perf_model/l2_cache/associativity=${l2_associativity} \
			-d ../../

python3 $DEFFE_DIR/example/extract_single_test_data.py | sed 's/:/ /g' | awk '{if( NR==1){print $NF}}' > results.out
