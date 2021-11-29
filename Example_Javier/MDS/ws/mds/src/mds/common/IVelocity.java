
package mds.common;

/**
 * This method is included in the class interface IVelocity and it gets state 
 * and changes it, It updates the values for the positions and the kinetical energy.
 * It returns the maximum displacement.
 */
public interface IVelocity {
  /**
   * Kinds of images that can be requested to the results formating module
   *  
   */
  public enum VelocityComputingAlgorithm {
    VERLET,/**
     * This indicates that the velocities and positions in a step are to be calculated using the Verlet algorithm.
     *  
     */

    LEAPFROG,/**
     * This indicates that the velocities and positions in a step are to be calculated using the Leap_Frog algorithm.
     */
;
  }

  double calcVelocity() ;

}
