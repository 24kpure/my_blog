package myWeibo;

/**
 * Created by ${lmj} on 2017/2/3.
 */

import java.util.Date;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

/**
 * 调用任务的类
 *
 * @author lhy
 */

public class cornTrigger {
    public static void main(String[] args) {

        //通过schedulerFactory获取一个调度器
        SchedulerFactory schedulerfactory = new StdSchedulerFactory();
        Scheduler scheduler = null;
        try {
            // 通过schedulerFactory获取一个调度器
            scheduler = schedulerfactory.getScheduler();

            //创建jobDetail实例，绑定Job实现类 指明job的名称，所在组的名称，以及绑定job类
            JobDetail job = JobBuilder.newJob(TimeTask_quartz.class).withIdentity("job1", "jgroup1").build();

            //    定义调度触发规则，每天上午10：42执行
            Trigger trigger = TriggerBuilder.newTrigger().withIdentity("simpleTrigger", "triggerGroup")
                    .withSchedule(CronScheduleBuilder.cronSchedule("0/3 38 22 * * ? *"))
                    .startNow().build();
            //    把作业和触发器注册到任务调度中
            scheduler.scheduleJob(job, trigger);

            //  启动调度
            scheduler.start();
            System.out.println(new Date());

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
