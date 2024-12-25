import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        int answer = 0;
        st = new StringTokenizer(br.readLine());
        int[] pos = new int[N];
        
        for (int i = 0; i < N; i++) {
            pos[i] = Integer.parseInt(st.nextToken());
        }
        
        // 배열 정렬
        Arrays.sort(pos);
        
        for (int i = 0; i < Q; i++) {
            int target = Integer.parseInt(br.readLine());
            int idx = Arrays.binarySearch(pos, target);
            
            if (idx < 0) {
                // 삽입 포인트 찾기
                idx = -idx - 1;
                
                // 근접한 값 계산
                int closest;
                if (idx == 0) {
                    // 배열의 첫 번째 값이 근접
                    closest = pos[0];
                } else if (idx == N) {
                    // 배열의 마지막 값이 근접
                    closest = pos[N - 1];
                } else {
                    // 이전 값과 현재 위치 값 중 더 가까운 값을 선택
                    int before = pos[idx - 1];
                    int after = pos[idx];
                    closest = (target - before <= after - target) ? before : after;
                }
                
                answer += closest;
            } else {
                // 값이 정확히 배열에 있으면 해당 값 추가
                answer += pos[idx];
            }
        }
        
        System.out.println(answer);
    }
}
