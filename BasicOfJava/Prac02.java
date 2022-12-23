public class Prac02 {

    public static void main(String[] args) throws Exception {

        //variable, type, System in, out

        // literal
//        int var1 = 0b1011;  // 2진수
//        int var2 = 0206;    // 8진수
//        int var3 = 365;     // 10진수
//        int var4 = 0xB3;    // 16진수

//        System.out.println("var1 : "+ var1);
//        System.out.println("var2 : "+ var2);
//        System.out.println("var3 : "+ var3);
//        System.out.println("var4 : "+ var4);



//        byte var1 = -128;
//        byte var2 = -30;
//        byte var3 = 0;
//        byte var4 = 30;
//        byte var5 = 127;
//        //byte var6 = 128;    // 컴파일 에러


//        //long balance = 30000000000; // 컴파일 에러
//        long balance = 30000000000L;


//        // char
//        char var1 = 'A';
//        char var2 = 'B';
//        char var3 = '가';
//        char var4 = '각';
//
//        char A = 65;
//
//        System.out.println(var1);
//        System.out.println(A);

        // ''로 감싼 문자리터럴은 유니코드로 변환되기 때문에 int타입 변수에도 저장가능
        // char타입 변수에 저장하면 자동으로 문자로 매핑되어 출력되지만,
        // int 타입 변수에 저장하면 유니코드 자체가 출력된다.
//        int A = 'A';
//        System.out.println(A);


        //"" 큰따옴표로 감싼 문자들을 문자열이라고 부르며,
        // 아래처럼은 동작하지않는다.
        // char var1 = "A";


        // float, double
//        float var1 = 0.1234567890123456789f;
//        double var2= 0.1234567890123456789;
//
//        System.out.println("float: " + var1);
//        System.out.println("double: " + var2);
//
//        double var3 = 3e6;
//        float var4 = 3e6F;
//        double var5 = 2e-3;
//        System.out.println("var3: " + var3);
//        System.out.println("var4: " + var4);
//        System.out.println("var5: " + var5);


//        long var1 = 2L;
//        float var2 = 1.8F;
//        double var3 = 2.5;
//        String var4 = "3.9";
//        int result = (int)var1 + (int)(var2 + var3) + (int)Double.parseDouble(var4);
//
//        System.out.println(result);


//        int value = 123;
//        System.out.printf("상품의 가격:%d원\n", value);
//        System.out.printf("상품의 가격:%6d원\n", value);
//        System.out.printf("상품의 가격:%-6d원\n", value);
//        System.out.printf("상품의 가격:%06d원\n", value);
//
//        double area = 3.14159 * 10 * 10;
//        System.out.printf("반지름이 %d인 원의 넓이:%10.2f\n", 10, area);
//
//        String name = "홍길동";
//        String job = "도적";
//
//        System.out.printf("%6d | %-10s | %10s\n", 1, name, job);


        // System in, out
//        int keyCode;
//
//        keyCode = System.in.read();
//        System.out.println("keyCode: " + keyCode);
//
//        keyCode = System.in.read();
//        System.out.println("keyCode: " + keyCode);
//
//        keyCode = System.in.read();
//        System.out.println("keyCode: " + keyCode);

//        int keyCode;
//
//        while(true){
//            keyCode = System.in.read();
//            System.out.println("keyCode: " + keyCode);
//            if(keyCode == 113){
//                break;
//            }
//        }

//        Scanner scanner = new Scanner(System.in);
//        String inputData;
//
//
//        while(true){
//            inputData = scanner.nextLine();
//            System.out.println("입력된 문자열: \"" + inputData + "\"");
//            if(inputData.equals("q")){
//                break;
//            }
//        }
//
//        System.out.println("종료");

//        Scanner scanner = new Scanner(System.in);
//        String name, regiNumber, phone;
//
//        System.out.println("[필수 정보 입력]");
//        System.out.print("1. 이름: ");
//        name = scanner.nextLine();
//        System.out.print("2. 주민번호 앞 6자리: ");
//        regiNumber = scanner.nextLine();
//
//        System.out.print("3. 전화번호: ");
//        phone = scanner.nextLine();
//
//        System.out.println("[입력한 내용]");
//        System.out.println(name);
//        System.out.println(regiNumber);
//        System.out.println(phone);



    }
}
