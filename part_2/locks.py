from threading import Semaphore


class Lock:
	# Implementation of reader-writer locks
	def __init__(self):
		self.__lock = Semaphore(1)
		self.__readers = Semaphore(1)
		self.__read_count = 0

	def reader_acquire(self):
		self.__lock.acquire()
		self.__read_count += 1

		if self.__read_count == 1:
			self.__readers.acquire()

		self.__lock.release()

	def reader_release(self):
		self.__lock.acquire()
		self.__read_count -= 1

		if self.__read_count == 0:
			self.__readers.release()

		self.__lock.release()

	def writer_acquire(self):
		self.__readers.acquire()

	def writer_release(self):
		self.__readers.release()
