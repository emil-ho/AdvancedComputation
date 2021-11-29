
package mds.common;

public class R3Point extends R2Point implements Cloneable {
  /**
   * Coordinate in the z axis for the three dimensional value
   *  
   */
  public double z;

  /**
   * Calculates the distance between two points in R3 space (module of the difference)
   * 
   * @param the point to which the distance will be calculated
   * @return the module of the distance between this and the point given as argument, 
   * it is returned as a double value.
   *  
   */
  public double distanceTo(R3Point r3Point) {
    	  return 0.0;
  }

  public R3Point(double x, double y, double z) {
    	  super(x,y);
    	  this.z = z;
  }

  public R3Point() {
    	  super();
  }

  /**
   * Returns a copy of the current object
   * 
   * @return a copy of the current object
   */
  public Object clone() {
            Object obj=null;
            try{
                obj=super.clone();
            }catch(Exception ex){  //Use CloneNotSupportedException if possible
                System.out.println(" It was not possible to clone...");
            }
            return obj;
  }

}
