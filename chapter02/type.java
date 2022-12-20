package chapter02;

public class type {

    public static void main(String[] args) {

        System.out.println("byte type");
        // byte(1byte, 8bit) -128 ~ 127
        byte b = 30;
        System.out.println(b);

        byte bMin = -128;
        byte bMax = 127;

        System.out.println(bMin +" ~ " + bMax);
        // b = 128; // error


        System.out.println("short type");
        // short(2byte, 16bit) -32,768 ~ 32,767
        short s = 30000;
        System.out.println(s);

        short sMin = -32767;
        short sMax = 32767;

        System.out.println(sMin +" ~ " + sMax);
        // s = -32769; // error



        System.out.println("char type");
        // char(2byte, 16bit) 0 ~ 65535(UNICODE)
        char c = 30000;
        System.out.println(c);

        // char c2 = -1; // error

        char cMin = 0;
        char cMax = 65535;

        System.out.println(cMin +" ~ " + cMax);
        // c = 65536; // error



        System.out.println("int type");
        // int(4byte, 32bit) -2,147,483,648 ~ 2,147,483,647
        int i = 2100000000;
        System.out.println(i);

        int iMin = -2147483648;
        int iMax = 2147483647;

        System.out.println(iMin +" ~ " + iMax);
        // i = 2147483648; // error



        System.out.println("long type");
        // long(8byte, 64bit) –9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
        long l = 9000000000000000000L;
        System.out.println(l);

                        // 기본적으로 정수 리터럴은 int 타입으로 간주하므로,
                        // L을 붙여 롱타입 리터럴임을 명시해 줘야 합니다.
        long lMin = -9223372036854775808L;
        long lMax = 9223372036854775807L;

        System.out.println(lMin +" ~ " + lMax);
        // l = –9223372036854775809; // error



        // 실수
        System.out.println("float type");

        // long(8byte, 64bit) –9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
        long l = 9000000000000000000L;
        System.out.println(l);

        // 기본적으로 정수 리터럴은 int 타입으로 간주하므로,
        // L을 붙여 롱타입 리터럴임을 명시해 줘야 합니다.
        long lMin = -9223372036854775808L;
        long lMax = 9223372036854775807L;

        System.out.println(lMin +" ~ " + lMax);
        // l = –9223372036854775809; // error








    }

}
