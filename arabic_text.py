import alphabet
from _types.linked_queue import LinkedQueue

class ArabicText(LinkedQueue):

  class ArabicTextChar:  
      def __init__(self, parent, node):
          self._node = node 
          self._parent = parent

      def __eq__(self, other):
          return self.char() == other
      
      def next(self):
          return self._parent.after(self)

      def prev(self):
          return self._parent.before(self)

      def char(self):
          return self._node._ele

      def is_blank(self):
        return self == ' '

      def is_word_start(self):
        return self._node is self._parent._head

      def is_alif(self):
        # NOTE: Alif with Wasla is pronounced differently based on whether
        # it is connected with the previous word or not; if it is connected
        # it is pronounced like an Lam, otherwise it is pronounced like
        # an Alif with Hamza above.
        return self == alphabet.ALIF or \
               self == alphabet.ALIF_WITH_WASLA_ABOVE or \
               self == alphabet.ALIF_KHANJAREEYA or \
               self == alphabet.ALIF_WITH_MADDA_ABOVE

      def is_al(self):
        """
        Determines whether there is an Alif followed by Lam at the given position.
        """
        return self.is_alif() and self.next() == alphabet.LAM

      def is_followed_by_sun(self):
          lam_node = self.next()
          if lam_node.next().is_followed_by_shadda():
              return lam_node.next().char()
          return False

      def is_followed_by_shadda(self):
          return self.next() == alphabet.SHADDA

      def is_fatha_followed_by_alif(self):
          try:
              return self == alphabet.FATHA and self.next().is_alif()
          except:
              return False

      def is_kasra_followed_by_ya(self):
        return self == alphabet.KASRA and self.next() == alphabet.YA

      def is_damma_followed_by_waw(self):
        return self == alphabet.DAMMA and self.next() == alphabet.WAW

  def __init__(self, text):
    super().__init__()
    for c in text:
        self.enqueue(c)

  def _make_position(self, node):
      if node is None:
          return None
      return self.ArabicTextChar(self, node)

  def first(self):
      return self._make_position(self._head)

  def after(self, p):
      return self._make_position(p._node._next)

  def before(self, p):
      return self._make_position(p._node._prev)

  def __iter__(self):
      cursor = self.first()
      while cursor is not None:
          self.cursor = cursor
          yield cursor
          cursor = self.after(cursor)
