package prac;

import java.util.regex.Pattern;

public class quiz1 {

    public static void main(String[] args) {

        int N = 11;
        solution(N);




    }


    public static void solution(int N){

        int quotient = 0;
        int remainder = 0;

        int temp1 = 0;
        int temp2 = 0;
        int temp3 = 0;

        quotient = N / 5; // 몫
        remainder = N % 5; // 나머지

        // 5로 나누어 떨어지면 N/5
        if(remainder == 0){
            System.out.println(N/5);
            return;
        }

        int i = 0;
        while (true){





            temp2 = 5 * (quotient - i);

            if(temp2 < 0){
                System.out.println("-1");
                    return;
            }

            temp3 = N - temp2;


            if((temp3%3) != 0){
                i++;
            }else{
                temp1 = temp3 / 3;

                temp3 = (quotient - i) + temp1;
                System.out.println(temp3);
                return;
            }


        }

    }
}
