
package mds.neighbours;

import mds.common.*;
import java.util.*;
/**
 * This class calculates the current neighbours lists for all particles.
 */
public class Neighbours implements mds.common.INeighbours {
  /**
   * The state for which the vecinities of all particles are calculated.
   * This value is initialized by the constructor.
   */
  protected mds.common.State s;

  /**
   * This static method returns a Neighbours object that implements the interface INeighbours
   * 
   * @param s the state for whose particles the vicinity will be calculated when needed
   * @return an object of a class that implements the interface INeighbours
   */
  public static mds.common.INeighbours createNeighbours(mds.common.State s)
  {
    	 
    		  return new Neighbours(s);
    
  }

  /**
   * This constructor receives the state for which the Neighbours object
   * will be created.
   * 
   * @param s the state for whose particles the vecinity will be calculated when needed
   */
  public Neighbours(mds.common.State s) {
          this.s = s;
  }

  /**
   * This methode verifies the need to recalculate the vecinity of the particles
   * and do it if necessary. 
   * It accumulates the maxDisplacements input argument and re-calculates the 
   * vecinities if the accumulated displacement exceeds the maximum tolerable.
   * If the vecinities need to be recalculated it calculates all the vecinities lists 
   * and reset the accumulated displacement to 0.0.
   * 
   * @param maxDisplacement the value of the largest displacement suffered in the 
   * ongoing step by any of the particles in the system.
   * @return true if the vecinities have been recalculated false otherwise
   */
  public boolean calcVecinity(double maxDisplacement) {
return false;
  }

}
