
import os
from trac.core import *
from trac.env import IEnvironmentSetupParticipant



class TracMetrixSetupParticipant(Component):
    """
        This class make sure that the enviroment has what TracMetrix Needs.
        
        1) The cache folder for chart
        2) Database
        3) Required plugins
    
    """
    implements(IEnvironmentSetupParticipant)
    
    
    def environment_created(self):
        """Called when a new Trac environment is created."""
        if self.environment_needs_upgrade(None):
            self.upgrade_environment(None)
            
            
    def environment_needs_upgrade(self, db):
        """Called when Trac checks whether the environment needs to be upgraded.
        
        Should return `True` if this participant needs an upgrade to be
        performed, `False` otherwise.
        """
        return (self._cachefolder_needs_upgrade())

    def upgrade_environment(self, db):
        """Actually perform an environment upgrade.
        
        Implementations of this method should not commit any database
        transactions. This is done implicitly after all participants have
        performed the upgrades they need without an error being raised.
        """
        
        def p(s):
            print s
            return True
        print "TracMetrix Plugin needs an upgrade"
        
        if self._cachefolder_needs_upgrade():
            p("creating cache folder")
            path = os.path.join(self.env.path, 'cache', 'tracmetrixplugin')
            os.makedirs(path) 
        print "Done Upgrading"
        
        
    def _cachefolder_needs_upgrade(self):
        # Check if the cache exist
        path = os.path.join(self.env.path, 'cache', 'tracmetrixplugin')
        return not os.path.exists(path)
        