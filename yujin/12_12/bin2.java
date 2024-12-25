import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long play = Long.parseLong(st.nextToken());
        long win = Long.parseLong(st.nextToken());
        long currentRate = win * 100 / play;

        if ((win + (long)Math.pow(10, 12)) * 100 / (play + (long)Math.pow(10, 12)) == currentRate) {
            System.out.println("X");
        } else {
            System.out.println(addPlay(play, win, 1, (long)Math.pow(10, 12), currentRate));
        }
    }

    public static long addPlay(long nowPlay, long nowWin, long minPlay, long maxPlay, long nowPercent) {
        if (minPlay > maxPlay) return minPlay;
        long middle = (minPlay + maxPlay) / 2;
        long middlePercent = (nowWin + middle) * 100 / (nowPlay + middle);

        if (middlePercent > nowPercent) {
            return addPlay(nowPlay, nowWin, minPlay, middle - 1, nowPercent);
        } else {
            return addPlay(nowPlay, nowWin, middle + 1, maxPlay, nowPercent);
        }
    }
}
