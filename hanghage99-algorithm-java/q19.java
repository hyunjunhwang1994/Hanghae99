import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class q19 {

    public static void main(String[] args) {

        String[] strings = {"sun", "bed", "car"};

        for(String s : strings){
            System.out.println(s);
        }

    }


    public static String[] solution(String[] strings, int n) {

        String[] answer ={};
        ArrayList<String> array = new ArrayList<>();

        for(int i=0; i<strings.length;i++){
            array.add("" + strings[i].charAt(n) + strings[i]);
        }

        Collections.sort(array);

        answer = new String[array.size()];

        for(int i = 0; i<array.size(); i++){
            answer[i] = array.get(i).substring(1, array.get(i).length());
        }
        return answer;



    }
}
