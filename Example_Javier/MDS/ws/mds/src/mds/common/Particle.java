
package mds.common;

import java.util.*;
public class Particle implements Cloneable {
  /**
   * Set of particles that due to their distances to the particle are in its vecinity. 
   */
  public Set<Particle> vecinity;

  public Particle(R3Point r, R3Point v, R3Point a) {
    this.r = r;
    this.v = v;
    this.a = a;  
  }

  /**
   * This constructor creates the particle assigning only the 
   * position of the particle using the coordinates given 
   * as arguments x, y and z. The velocity and the acceleration
   * are also created but initialized with 0.0
   */
  public Particle(double x, double y, double z) {
    	  this.r = new R3Point(x,y,z);
    	  this.v = new R3Point(0.0,0.0,0.0);
    	  this.a = new R3Point(0.0,0.0,0.0);
    
    
  }

  /**
   * This constructor creates the particle assigning all internal variables in zero
   * plus and empty new vecinity
   */
  public Particle() {
    	  this.r = new R3Point(0.0,0.0,0.0);
    	  this.v = new R3Point(0.0,0.0,0.0);
    	  this.a = new R3Point(0.0,0.0,0.0);
              this.vecinity = new HashSet<Particle> ();
    
    
  }

  /**
   * Returns a copy of the current object
   * 
   * @return a copy of the current object
   */
  public Object clone() {
                Particle obj=null;
                try{
                    obj=(Particle) super.clone();
                    obj.a = (R3Point) obj.a.clone();
                    obj.v = (R3Point) obj.v.clone();
                    obj.r = (R3Point) obj.r.clone();
                }catch(CloneNotSupportedException ex){
                    System.out.println(" It was not possible to clone...");
                }
                return obj;
  }

  /**
   * The position of the particle
   *  
   */
  public R3Point r;

  /**
   * he velocity of the particle
   *  
   */
  public R3Point v;

  /**
   * The acceleration of the particle
   *  
   */
  public R3Point a;

  /**
   * The maximum possible displacement of the particle since the last
   * time the vecinity has been calculated. This attribute is updated by
   * the velocity calculation module at each step. It is reset to 0.0 
   * by the neighbours module when the vecinity is recalculated.
   */
  public double d;

}
