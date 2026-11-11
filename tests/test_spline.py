import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import spline
class TestSpline(unittest.TestCase):
 def setUp(self):
  self.p=np.array([[0,0],[1,2],[2,1],[3,3],[4,0]],float); self.t,self.cx,self.cy=spline.construir(self.p)
 def test_interpolation(self):
  self.assertTrue(np.allclose(spline.evaluar(self.t,self.cx,self.t),self.p[:,0]))
  self.assertTrue(np.allclose(spline.evaluar(self.t,self.cy,self.t),self.p[:,1]))
 def test_continuity(self):
  e=spline.errores_continuidad(self.t,self.cx,self.cy)
  self.assertLess(e["C0"],1e-8); self.assertLess(e["C1"],1e-8); self.assertLess(e["C2"],1e-8)
if __name__=="__main__": unittest.main()
