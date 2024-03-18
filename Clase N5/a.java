import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class a {
    // Método para convertir a binario
    public static String toBinary(int number) {
        StringBuilder binary = new StringBuilder();
        while (number > 0) {
            int remainder = number % 2;
            binary.insert(0, remainder);
            number = number / 2;
        }
        return binary.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        List<Double> timeList = new ArrayList<>();

        System.out.print("¿Cuántos números tendrá el vector?: ");
        int n = scanner.nextInt();

        for (int i = 0; i < 4; i++) {
            long startTime = System.nanoTime();

            int[] vector = new int[n];
            for (int j = 0; j < n; j++) {
                vector[j] = random.nextInt(9000) + 1001; // Números de 4 dígitos
            }

            // Convertir los números a binario
            for (int num : vector) {
                toBinary(num);
            }

            long endTime = System.nanoTime();
            double time = ((endTime - startTime) / 1e6)/1000.0; // Convertir a milisegundos
            timeList.add(time);
        }

        // Imprimir tiempos y n
        System.out.println("Tiempos de ejecución: " + timeList);
        System.out.println("n = " + n);
    }
}
