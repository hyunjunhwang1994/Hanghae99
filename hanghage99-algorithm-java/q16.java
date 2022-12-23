import java.util.*;


public class q16 {

    public static void main(String[] args) {



    }



    public static int[] solution(int[] numbers){

        ArrayList<Integer> arr = new ArrayList<>();

        int len = numbers.length;
        int temp;

        for(int i=0; i<len-1; i++){

            for(int j=i+1; j<len; j++){
                temp = numbers[i] + numbers[j];
                if (arr.indexOf(temp) < 0) {
                    arr.add(temp);
                }
            }

        }

        int answer[] = new int[arr.size()];
        for(int i=0;i<answer.length; i++)
            answer[i] = arr.get(i);
        Arrays.sort(answer);
        return answer;

    }
}
