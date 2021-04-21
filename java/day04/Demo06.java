package day04;

public class Demo06 {
    public static void main(String[] args) {
        AlarmDoor ad = new AlarmDoor();
        ad.open();
        ad.close();
        ad.alarm();

        PutongDoor pd =new PutongDoor();
        pd.close();
        pd.open();
    }
}
/*
门：抽象类，开门、关门的功能
警报：接口，报警的接口
防盗门：从门继承，实现开门，关门的功能，实现报警的接口。
普通门：从门继承，实现开门，关门的功能。
 */
abstract class Door{
    public abstract void open();
    public abstract void close();
}
interface Alarm{
    void alarm();//报警的功能
}
interface usb{
    void usb();//usb充电的功能
}
//                              可以实现多个功能
class AlarmDoor extends Door implements Alarm,usb{

    @Override
    public void open() {
        System.out.println("指纹校验通过，开门");
    }

    @Override
    public void close() {
        System.out.println("三道锁全部关闭");
    }

    @Override
    public void alarm() {
        System.out.println("警告,有陌生人靠近");
    }

    @Override
    public void usb() {
        System.out.println("充电......");
    }
}

class PutongDoor extends Door {

    @Override
    public void open() {
        System.out.println("一推就开");
    }

    @Override
    public void close() {
        System.out.println("一推就关");
    }
}
