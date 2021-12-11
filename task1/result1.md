# Задание 1

## Локальный запус

wiki.txt
```
No configs found; falling back on auto-configuration
No configs specified for inline runner
Running step 1 of 1...
Creating temp directory /tmp/job.hadoop.20211207.164202.072790
job output is in results/result_local
Removing temp directory /tmp/job.hadoop.20211207.164202.072790...

real	1m25,490s
user	1m23,509s
sys	0m1,957s
```

wiki\_trunc.txt
```
No configs found; falling back on auto-configuration
No configs specified for inline runner
Running step 1 of 1...
Creating temp directory /tmp/job.hadoop.20211207.164920.033606
job output is in results/result_local_trunc
Removing temp directory /tmp/job.hadoop.20211207.164920.033606...

real	0m2,567s
user	0m2,468s
sys	0m0,092s
```

## Hadoop

wiki.txt
```
No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in /home/hadoop/hadoop/bin...
Found hadoop binary: /home/hadoop/hadoop/bin/hadoop
Using Hadoop version 3.3.0
Looking for Hadoop streaming jar in /home/hadoop/hadoop...
Found Hadoop streaming jar: /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar
Creating temp directory /tmp/job.hadoop.20211207.164525.872252
uploading working dir files to hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.164525.872252/files/wd...
Copying other local files to hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.164525.872252/files/
Running step 1 of 1...
  packageJobJar: [/tmp/hadoop-unjar4398052783522274830/] [] /tmp/streamjob9742425474563085167.jar tmpDir=null
  Connecting to ResourceManager at /0.0.0.0:8032
  Connecting to ResourceManager at /0.0.0.0:8032
  Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1638893868055_0002
  Total input files to process : 1
  number of splits:2
  Submitting tokens for job: job_1638893868055_0002
  Executing with tokens: []
  resource-types.xml not found
  Unable to find 'resource-types.xml'.
  Submitted application application_1638893868055_0002
  The url to track the job: http://X1-Carbon:8088/proxy/application_1638893868055_0002/
  Running job: job_1638893868055_0002
  Job job_1638893868055_0002 running in uber mode : false
   map 0% reduce 0%
   map 28% reduce 0%
   map 29% reduce 0%
   map 36% reduce 0%
   map 47% reduce 0%
   map 53% reduce 0%
   map 55% reduce 0%
   map 66% reduce 0%
   map 67% reduce 0%
   map 81% reduce 0%
   map 89% reduce 0%
   map 100% reduce 0%
   map 100% reduce 100%
  Job job_1638893868055_0002 completed successfully
  Output directory: hdfs:///user/hadoop/result_hadoop
Counters: 54
	File Input Format Counters 
		Bytes Read=113415480
	File Output Format Counters 
		Bytes Written=9551989
	File System Counters
		FILE: Number of bytes read=92468885
		FILE: Number of bytes written=129411262
		FILE: Number of large read operations=0
		FILE: Number of read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=113415668
		HDFS: Number of bytes read erasure-coded=0
		HDFS: Number of bytes written=9551989
		HDFS: Number of large read operations=0
		HDFS: Number of read operations=11
		HDFS: Number of write operations=2
	Job Counters 
		Data-local map tasks=2
		Launched map tasks=2
		Launched reduce tasks=1
		Total megabyte-milliseconds taken by all map tasks=135675904
		Total megabyte-milliseconds taken by all reduce tasks=8155136
		Total time spent by all map tasks (ms)=132496
		Total time spent by all maps in occupied slots (ms)=132496
		Total time spent by all reduce tasks (ms)=7964
		Total time spent by all reduces in occupied slots (ms)=7964
		Total vcore-milliseconds taken by all map tasks=132496
		Total vcore-milliseconds taken by all reduce tasks=7964
	Map-Reduce Framework
		CPU time spent (ms)=155490
		Combine input records=9606774
		Combine output records=1615127
		Failed Shuffles=0
		GC time elapsed (ms)=100
		Input split bytes=188
		Map input records=12601
		Map output bytes=343593599
		Map output materialized bytes=36135657
		Map output records=8623816
		Merged Map outputs=2
		Peak Map Physical memory (bytes)=395472896
		Peak Map Virtual memory (bytes)=2860982272
		Peak Reduce Physical memory (bytes)=298381312
		Peak Reduce Virtual memory (bytes)=2772422656
		Physical memory (bytes) snapshot=1015713792
		Reduce input groups=472189
		Reduce input records=632169
		Reduce output records=472189
		Reduce shuffle bytes=36135657
		Shuffled Maps =2
		Spilled Records=2247296
		Total committed heap usage (bytes)=786432000
		Virtual memory (bytes) snapshot=8322097152
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
job output is in hdfs:///user/hadoop/result_hadoop
Removing HDFS temp directory hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.164525.872252...
Removing temp directory /tmp/job.hadoop.20211207.164525.872252...

real	1m37,144s
user	0m28,919s
sys	0m1,338s
```

wiki_trunc.txt
```
No configs found; falling back on auto-configuration
No configs specified for hadoop runner
Looking for hadoop binary in /home/hadoop/hadoop/bin...
Found hadoop binary: /home/hadoop/hadoop/bin/hadoop
Using Hadoop version 3.3.0
Looking for Hadoop streaming jar in /home/hadoop/hadoop...
Found Hadoop streaming jar: /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar
Creating temp directory /tmp/job.hadoop.20211207.165000.441888
uploading working dir files to hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.165000.441888/files/wd...
Copying other local files to hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.165000.441888/files/
Running step 1 of 1...
  packageJobJar: [/tmp/hadoop-unjar5124642332379143038/] [] /tmp/streamjob148341792720705762.jar tmpDir=null
  Connecting to ResourceManager at /0.0.0.0:8032
  Connecting to ResourceManager at /0.0.0.0:8032
  Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1638893868055_0003
  Total input files to process : 1
  number of splits:2
  Submitting tokens for job: job_1638893868055_0003
  Executing with tokens: []
  resource-types.xml not found
  Unable to find 'resource-types.xml'.
  Submitted application application_1638893868055_0003
  The url to track the job: http://X1-Carbon:8088/proxy/application_1638893868055_0003/
  Running job: job_1638893868055_0003
  Job job_1638893868055_0003 running in uber mode : false
   map 0% reduce 0%
   map 100% reduce 0%
   map 100% reduce 100%
  Job job_1638893868055_0003 completed successfully
  Output directory: hdfs:///user/hadoop/result_hadoop_trunc
Counters: 54
	File Input Format Counters 
		Bytes Read=2700352
	File Output Format Counters 
		Bytes Written=824890
	File System Counters
		FILE: Number of bytes read=2916012
		FILE: Number of bytes written=6638783
		FILE: Number of large read operations=0
		FILE: Number of read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2700552
		HDFS: Number of bytes read erasure-coded=0
		HDFS: Number of bytes written=824890
		HDFS: Number of large read operations=0
		HDFS: Number of read operations=11
		HDFS: Number of write operations=2
	Job Counters 
		Data-local map tasks=2
		Launched map tasks=2
		Launched reduce tasks=1
		Total megabyte-milliseconds taken by all map tasks=7284736
		Total megabyte-milliseconds taken by all reduce tasks=2184192
		Total time spent by all map tasks (ms)=7114
		Total time spent by all maps in occupied slots (ms)=7114
		Total time spent by all reduce tasks (ms)=2133
		Total time spent by all reduces in occupied slots (ms)=2133
		Total vcore-milliseconds taken by all map tasks=7114
		Total vcore-milliseconds taken by all reduce tasks=2133
	Map-Reduce Framework
		CPU time spent (ms)=4430
		Combine input records=199390
		Combine output records=50284
		Failed Shuffles=0
		GC time elapsed (ms)=54
		Input split bytes=200
		Map input records=50
		Map output bytes=8192039
		Map output materialized bytes=2916018
		Map output records=199390
		Merged Map outputs=2
		Peak Map Physical memory (bytes)=313970688
		Peak Map Virtual memory (bytes)=2770882560
		Peak Reduce Physical memory (bytes)=237187072
		Peak Reduce Virtual memory (bytes)=2772492288
		Physical memory (bytes) snapshot=854884352
		Reduce input groups=40362
		Reduce input records=50284
		Reduce output records=40362
		Reduce shuffle bytes=2916018
		Shuffled Maps =2
		Spilled Records=100568
		Total committed heap usage (bytes)=780140544
		Virtual memory (bytes) snapshot=8312045568
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
job output is in hdfs:///user/hadoop/result_hadoop_trunc
Removing HDFS temp directory hdfs:///user/hadoop/tmp/mrjob/job.hadoop.20211207.165000.441888...
Removing temp directory /tmp/job.hadoop.20211207.165000.441888...

real	0m28,807s
user	0m28,580s
sys	0m1,226s
```
