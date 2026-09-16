package practicas1y2;

public class AlgebraVectorial {
	//perpendicularidad por valor abs
	public boolean esPerpendicular(Vector3D a, Vector3D b) {
		Vector3D vectorSuma = a.suma(b);
		Vector3D vectorResta = a.resta(b);
		double diferencia = Math.abs(vectorSuma.longitud() - vectorResta.longitud());
		return diferencia < 0.0001;
	}
	
	//perpendicularidad por producto punto
	public boolean esPerpendicular(Vector3D a, Vector3D b, String modo) {
		if(modo.equalsIgnoreCase("punto")) {
			return Math.abs(a.multiEscalar(b)) < 0.0001;
		}else if(modo.equalsIgnoreCase("pitagoras")) {
			double izq = Math.pow(a.suma(b).longitud(), 2);
			double der = Math.pow(a.longitud(), 2) + Math.pow(b.longitud(), 2);
			return Math.abs(izq - der) < 0.0001;
		} else {
			return false;
		}
	}
	
	//paralelismo por producto cruz
	public boolean esParalelo(Vector3D a, Vector3D b) {
	    Vector3D cruz = a.productoVectorial(b);
	    return Math.abs(cruz.longitud()) < 0.0001;
	}

	// paralelismo por multiescalar
	public boolean esParalelo(Vector3D a, Vector3D b, double r) {
	    Vector3D bEscalado = b.multiEscalar(r);
	    
	    double d1 = Math.abs(a.getA1() - bEscalado.getA1());
	    double d2 = Math.abs(a.getA2() - bEscalado.getA2());
	    double d3 = Math.abs(a.getA3() - bEscalado.getA3());
	    
	    return (d1 < 0.0001) && (d2 < 0.0001) && (d3 < 0.0001);
	}

	//PROYECCIÓN Y COMPONENTE
	
	//proyeccion
	public Vector3D proyAenB(Vector3D a, Vector3D b) {
	    double pEscalar = a.multiEscalar(b);
	    double modBSq = Math.pow(b.longitud(), 2);
	    double factor = pEscalar / modBSq;
	    
	    return b.multiEscalar(factor);
	}
	//componente
	public double compAenB(Vector3D a, Vector3D b) {
	    double pEscalar = a.multiEscalar(b);
	    double modB = b.longitud();
	    
	    return pEscalar / modB;
	}
}
