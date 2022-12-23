import java.util.ArrayList;
import java.util.Arrays;

public class q2 {


    public static void main(String[] args) {

        int[] arr = {5,10,1,2,4,33,235};
        int divisor = 5;



        for(int a : solution(arr, divisor)){
            System.out.println(a);
        }

    }

    public static int[] solution(int[] arr, int divisor){
        int count = 0;



        for(int i = 0; i < arr.length; i++){

            if(arr[i] % divisor == 0){
                count++;
            }

        }


        if(count == 0){
            int[] answer = {-1};
            return answer;
        }


        int[] answer = new int[count];

        for(int i = 0,j = 0; i < arr.length; i++){


             if (arr[i] % divisor == 0) {
                 answer[j] = arr[i];
                j++;

            }

        }


        Arrays.sort(answer);


        return answer;
    }










}
