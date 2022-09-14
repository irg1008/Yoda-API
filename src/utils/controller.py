from abc import abstractmethod


class Controller:
    loaded = False

    def __call__(self):
        if not self.loaded:
            self.loaded = True
            self._load()
        return self

    @abstractmethod
    def _load(
        self,
    ):
        """Here we implement everything that we need to load in the child controller.

        Raises:
            NotImplementedError: This method must be implemented in the child controller.
        """
        raise NotImplementedError
