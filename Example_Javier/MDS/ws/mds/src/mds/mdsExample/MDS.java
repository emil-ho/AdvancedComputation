
package mds.mdsExample;

import mds.common.*;
class MDS {
  /**
   * A main program used to run a simulation
   */
  public static void main(String [] args)
  {
    		// data source by default
    		String s = "data.txt";
    
    		// this gets the first input argument
    		if (args.length!=0 && args[0]!=null) {
    			s=args[0];
    		}
    
    		//takes the argument as the name of a file to open and read its content in InputData
    		InputData in;
    		try {
    			in = new InputData(s);
    		} catch (InputData.ExperimentNotCreated e) {
    			// TODO Auto-generated catch block
    			e.printStackTrace();
    			return;
    		}
    
    		//start a concurrent simulation
    
    		mds.common.IMDS sim = mds.mdsExample.MDSRun.createSimulator();
    
    		if (!sim.startSimulation(in)){
    			System.err.println("The simulation could not be started");
    			return;
    		}
    
    		//wait for the simulation to finish.
    
    		double fraction=0.0;
    		int percent = 0;
    		System.out.print("["); 	System.out.flush();
    		while ((fraction)<1.0){
    
    			try {
    				Thread.sleep(100);
    			} catch (InterruptedException e) {
    				// TODO Auto-generated catch block
    				e.printStackTrace();
    			}
    			fraction = sim.currentSimulationFraction();
    			int newDato = (int) (10.0*fraction);
    
    			if (newDato > percent){
    				percent = newDato;
    				System.out.printf("%4d%%", percent*10);
    				System.out.flush();
    			}
    		}
    
    		System.out.print("]");
    		System.out.flush();
    
    
    
    
  }

}
