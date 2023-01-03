package Date230103;


import java.util.*;

// 2023 01월 03일
// https://school.programmers.co.kr/learn/courses/30/lessons/42889
// 실패율
public class Main {
    public static void main(String[] args) {

        int n = 5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        Main app = new Main();



    int[] array = app.solution(n, stages);

        for (int i : array) {
            System.out.println(i);
        }



    }


    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] stageCount = new int[N];


        Map<Integer, Double> fail = new HashMap<>();
        int total = stages.length;

        for (int i = 0; i < stages.length; i++) {
            if (stages[i] == N + 1) { // 마지막 스테이지를 클리어한 것은 제외
                continue;
            }
            stageCount[stages[i] - 1]++;
        }

        for (int i = 0 ; i < stageCount.length; i++) {
            if (total == 0) {
                fail.put(i, 0d);
                continue;
            }
            fail.put(i, (double)stageCount[i] / (double)total);
            total -= stageCount[i];
        }

        for (int i = 0; i < N; i++) {
            double max = -1;
            int maxKey = 0;

            for (int key : fail.keySet()) {
                if (max < fail.get(key)) {
                    max = fail.get(key);
                    maxKey = key;
                }
            }

            answer[i] = maxKey + 1;
            fail.remove(maxKey);
        }

        return answer;

    }

}
