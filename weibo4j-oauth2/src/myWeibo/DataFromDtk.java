package myWeibo;

import weibo4j.org.json.JSONException;
import weibo4j.org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

/**
 * Created by ${lmj} on 2017/1/23.
 */
public class DataFromDtk {
    public JSONObject getDataByPage(int page) {
        String dtkUrl = "http://api.dataoke.com/index.php?r=goodsLink/qq&type=qq_quan&appkey=4zrn1r242o&v=2&page=";
        dtkUrl = dtkUrl + page;
        StringBuffer strBuf = new StringBuffer();
        try {
            URL url = new URL(dtkUrl);
            URLConnection conn = url.openConnection();
            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                strBuf.append(line + " ");
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        JSONObject myobject = null,data=null;
        try {
            //将字符串转换成jsonObject对象
            myobject = new JSONObject(strBuf.toString());
            data=(JSONObject) myobject.get("data");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return data;
    }
}
