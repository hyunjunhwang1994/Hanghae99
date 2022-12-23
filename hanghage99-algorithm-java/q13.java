import java.util.ArrayList;

public class q13 {

    public static void main(String[] args) {

        System.out.println(solution(45));


    }


    public static int solution(int n){
        int answer = 0;

        ArrayList<Integer> list = new ArrayList<>();

        while (true){
            if(n<3){list.add(n); break;}
            list.add(n%3);
            n= n/3;
        }

        for(int i=0; i<list.size(); i++){
            answer += (Math.pow(3, list.size()-i-1)*list.get(i));
        }

return answer;

    }

}
