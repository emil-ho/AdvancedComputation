
package mds.init;

import mds.common.*;
import java.util.*;
public class Init implements mds.common.IInit {
  /**
   * This is a graph with the histogram of velocities as they are 
   * assigned at the initialization of the lattice. It gets its
   * value at the end of the doInit operation.
   */
  protected mds.common.Graph initialVelocityDistribution;

  /**
   * This static method returns an InitModule object that implements the interface IInit.
   * 
   * @return an object that implements the interface IInit
   */
  public static mds.common.IInit createInit()
  {
    return new Init();
  }

  /**
   * Create the initial state for the given experiment and returns it with the 
   * initial positions, velocities and neighbours lists for all particles.
   * 
   * @param experiment is the experiment object with the data needed to configure and 
   * run the simulation
   * @return a fresh new State ready to start the simulation
   */
  public mds.common.State doInit(mds.common.InputData experiment) {
    return new State();
  }

  /**
   * Calculates a Graph showing the statistical distribution of velocities for 
   * all the particles of the system at the given state.
   * 
   * @param s areference to the State object for which the distribution will be calculated
   * @return a reference to the Graph object that holds the velocities distribution function 
   */
  public mds.common.Graph velocityDistribution(mds.common.State s) {
    return null;
  }

  /**
   * Returns a Graph showing the statistical distribution of velocities for 
   * all the particles of the system as they were assigned at the initial state.
   * 
   * @return a reference to the Graph object that holds the velocities distribution function 
   */
  public mds.common.Graph getInitialVelocityDistribution() {
        return initialVelocityDistribution;
  }

}
