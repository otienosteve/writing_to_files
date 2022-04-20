import unittest
import classsamp
class SampTest(unittest.TestCase):
  def test_instance(self):
    user=classsamp.User()
    self.assertInstance(user,classsamp.User)



if __name__=="__main__":
    unittest.main()


