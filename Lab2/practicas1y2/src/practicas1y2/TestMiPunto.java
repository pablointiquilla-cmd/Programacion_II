package practicas1y2;

public class TestMiPunto {
	public static void main(String[] args) {
		MiPunto p1 =  new MiPunto();
		MiPunto p2 = new MiPunto(10, 30.5);
		
		System.out.println("Punto 1: " + p1);
		System.out.println("Punto 2: " + p2);
		
		double dist = p1.distancia(p2);
			System.out.println("distancia: " + dist);
	}
}
