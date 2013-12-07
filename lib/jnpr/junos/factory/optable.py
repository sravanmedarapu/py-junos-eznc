# local
from .table import Table

class OpTable(Table):

  ### -------------------------------------------------------------------------
  ### PUBLIC METHODS
  ### -------------------------------------------------------------------------

  def get(self, *vargs, **kvargs):
    """ 
    Retrieve the XML table data from the Device instance and
    returns back the Table instance - for call-chaining purposes.  

    ALIAS: __call__    

    :vargs:
      [0] is the table :arg_key: value.  This is used so that
      the caller can retrieve just one item from the table without
      having to know the Junos RPC argument.

    :kvargs:
      these are the name/value pairs relating to the specific Junos
      XML command attached to the table.  For example, if the RPC 
      is 'get-route-information', there are parameters such as
      'table' and 'destination'.  Any valid RPC argument can be
      passed to :kvargs: to further filter the results of the :get():
      operation.  neato!

    NOTES:
      If you need to create a 'stub' for unit-testing
      purposes, you want to create a subclass of your table and 
      overload this methods.
    """

    argkey = vargs[0] if len(vargs) else None

    rpc_args = {}                     # create empty <dict>
    rpc_args.update(self.GET_ARGS)    # copy default args
    rpc_args.update(kvargs)           # copy caller provided args

    if hasattr(self, 'GET_KEY') and argkey is not None:
      rpc_args.update({self.GET_KEY: argkey })

    # execute the Junos RPC to retrieve the table
    self.xml = getattr(self.RPC,self.GET_RPC)(**rpc_args)

    # returning self for call-chaining purposes, yo!
    return self
