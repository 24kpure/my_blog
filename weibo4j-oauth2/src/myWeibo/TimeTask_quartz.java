package myWeibo;
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import weibo4j.examples.oauth2.Log;

import java.util.Date;

/**
 * Created by ${lmj} on 2017/2/3.
 */
public class TimeTask_quartz implements Job{
    @Override
    public void execute(JobExecutionContext arg0) throws JobExecutionException {
        Log.logInfo("开始执行定时任务---当前时间："+new Date());
        SendWeibo.main(null);

        Log.logInfo("定时任务执行完成---当前时间："+new Date());
        Log.logInfo("-------------------------------------");
    }
}
