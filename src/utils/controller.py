from abc import abstractmethod


class Controller:
    _loaded = False

    def __call__(self):
        if not self._loaded:
            self._loaded = True
            self._load()
        return self

    @property
    def loaded(self):
        return self._loaded

    @abstractmethod
    def _load(
        self,
    ):
        """Here we implement everything that we need to load in the child controller.

        Raises:
            NotImplementedError: This method must be implemented in the child controller.
        """
        raise NotImplementedError
