import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el valor de N: ");
        int n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            ArrayList<Integer> vector = new ArrayList<>();

            if (i % 2 == 0) {
                for (int j = 1; j <= i / 2; j++) {
                    if (i % j == 0) {
                        vector.add(j);
                    }
                }
            } else {
                for (int j = 1; j <= i / 3; j++) {
                    if (i % j == 0) {
                        vector.add(j);
                    }
                }
            }

            int sum = 0;
            for (int num : vector) {
                sum += num;
            }

            if (sum == i) {
                System.out.println("Número perfecto encontrado: " + i);
            }
        }
    }
}
