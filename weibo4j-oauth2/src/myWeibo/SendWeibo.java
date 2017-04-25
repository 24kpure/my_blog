package myWeibo;

import weibo4j.Timeline;
import weibo4j.examples.oauth2.Log;
import weibo4j.http.ImageItem;
import weibo4j.model.Status;
import weibo4j.model.WeiboException;
import weibo4j.org.json.JSONArray;
import weibo4j.org.json.JSONException;
import weibo4j.org.json.JSONObject;
import weibo4j.util.URLEncodeUtils;
import javax.imageio.stream.FileImageInputStream;
import java.io.*;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;
import java.util.concurrent.ThreadPoolExecutor;


/**
 * Created by ${lmj} on 2017/1/19.
 */
public class SendWeibo {
    public static void main(String[] args) {
        //自己的号String accessToken = "2.00FDWjZGNFq2GB2a2882f911Fl5ZIB";
        //二师兄
        String accessToken = "2.00FDWjZGNFq2GB7ff66f776188PzwB";
        DataFromDtk dtk = new DataFromDtk();
        JSONObject data = dtk.getDataByPage(1);
        try {
            int total_num = data.getInt("total_num");
            JSONArray resultArray = (JSONArray) data.get("result");
            int i = 0;
            while (i < total_num && i<=49)
                try {
                    JSONObject result = (JSONObject) resultArray.get(i);
                    String content = result.getString("D_title") + "\n券后：" + result.getString("Price") + "元\n"+result.getString("Quan_price")+"元券：" + result.getString("Quan_m_link") + "\n下单：" + result.getString("ali_click");
                    sendWeiboWithPicture(accessToken, content, result.getString("Pic"));
                    Log.logInfo("当前进度：" +(i+1)+"/"+(total_num));
                    Thread.currentThread().sleep(12*60*1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } finally {
                    i++;
                }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }


    public static boolean sendWeiboWithPicture(String accessToken, String content, String pictureUrl) {
        Timeline tl = new Timeline(accessToken);
        content = URLEncodeUtils.encodeURL(content);
        boolean result = false;
        try {
            //Status status = tl.uploadStatus(content, (new ImageItem(imageTobyte(pictureUrl))));
            Status status = tl.uploadStatus(content, (new ImageItem(netImageTobyte(pictureUrl))));
            Log.logInfo(status.toString());
            result = true;
        } catch (WeiboException e) {
            e.printStackTrace();
        }
        return result;
    }

    //本地路径图片
    public static byte[] imageTobyte(String url) {
        byte[] data = null;
        try {
            FileImageInputStream input = new FileImageInputStream(new File(url));
            ByteArrayOutputStream output = new ByteArrayOutputStream();
            byte[] buf = new byte[1024];
            int numBytesRead = 0;
            while ((numBytesRead = input.read(buf)) != -1) {
                output.write(buf, 0, numBytesRead);
            }
            data = output.toByteArray();
            output.close();
            input.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }

    public static LinkedList fileList(String pathName) {
        LinkedList linkList = new LinkedList<String>();
        File fileFloder = new File(pathName);
        File[] array = fileFloder.listFiles();
        for (File photo : array) {
            linkList.add(photo.getPath());
        }
        return linkList;
    }

    //网络路径图片
    public static byte[] netImageTobyte(String imageUrl) {
        byte[] data = null;
        try {
            URL url = new URL(imageUrl);
            URLConnection conn = url.openConnection();
            InputStream input = conn.getInputStream();
            ByteArrayOutputStream output = new ByteArrayOutputStream();
            byte[] buf = new byte[1024];
            int numBytesRead = 0;
            while ((numBytesRead = input.read(buf)) != -1) {
                output.write(buf, 0, numBytesRead);
            }
            data = output.toByteArray();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return data;
    }
}
