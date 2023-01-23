import unittest
from copy_paste import copy_paste


class TestCopyPaste(unittest.TestCase):
    def test_valid_type_output(self):
        self.assertIsInstance(
            copy_paste(
                "the first[CTRL+C] Coding Challenge was [CTRL+V] string manipulation task"
            ),
            str,
        )

    def test_empty_paste(self):
        self.assertEqual(
            copy_paste(
                "the first Coding Challenge was [CTRL+V] string manipulation task"
            ),
            "the first Coding Challenge was  string manipulation task",
        )

    def test_copy_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+C] Coding Challenge was [CTRL+V] string manipulation task"
            ),
            "the first Coding Challenge was the first string manipulation task",
        )

    def test_multi_copy_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+C] Coding Challenge[CTRL+C] was [CTRL+V] string manipulation task"
            ),
            "the first Coding Challenge was the first Coding Challenge string manipulation task",
        )

    def test_cut_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+X] Coding Challenge was [CTRL+V] string manipulation task"
            ),
            " Coding Challenge was the first string manipulation task",
        )

    def test_multi_cut_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+X] Coding Challenge[CTRL+X] was [CTRL+V] string manipulation task"
            ),
            " was  Coding Challenge string manipulation task",
        )

    def test_combination_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+X] Coding Challenge[CTRL+C] was [CTRL+V] string manipulation task"
            ),
            " Coding Challenge was  Coding Challenge string manipulation task",
        )

    def test_multi_empty_paste(self):
        self.assertEqual(
            copy_paste(
                "the first Coding Challenge[CTRL+V] was [CTRL+V] string manipulation task"
            ),
            "the first Coding Challenge was  string manipulation task",
        )

    def test_copy_multi_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+C] Coding Challenge[CTRL+V] was [CTRL+V] string manipulation task"
            ),
            "the first Coding Challengethe first was the first string manipulation task",
        )

    def test_cut_multi_paste(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+X] Coding Challenge[CTRL+V] was [CTRL+V] string manipulation task"
            ),
            " Coding Challengethe first was the first string manipulation task",
        )

    def test_combination(self):
        self.assertEqual(
            copy_paste(
                "the first[CTRL+X] Coding Challenge[CTRL+V] was [CTRL+V] string[CTRL+C] manipulation[CTRL+C] task[CTRL+V]"
            ),
            " Coding Challengethe first was the first string manipulation task Coding Challengethe first was the first string manipulation",
        )

    def test_big_combination(self):
        self.assertEqual(
            copy_paste(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.[CTRL+X] Mauris laoreet risus et bibendum cursus.[CTRL+X] Maecenas in rhoncus libero.[CTRL+V] Nunc convallis nunc non porttitor aliquet.[CTRL+C] Suspendisse odio elit, commodo ac tincidunt at, tempus feugiat enim. Morbi eu dolor metus.[CTRL+C] Mauris dictum convallis commodo.[CTRL+V] Pellentesque vitae purus sit amet nisi vulputate egestas at at urna.[CTRL+C] Fusce quam lacus, posuere et tortor eu, aliquet mollis nisi.[CTRL+V]"
            ),
            " Maecenas in rhoncus libero. Mauris laoreet risus et bibendum cursus. Nunc convallis nunc non porttitor aliquet. Suspendisse odio elit, commodo ac tincidunt at, tempus feugiat enim. Morbi eu dolor metus. Mauris dictum convallis commodo. Maecenas in rhoncus libero. Mauris laoreet risus et bibendum cursus. Nunc convallis nunc non porttitor aliquet. Suspendisse odio elit, commodo ac tincidunt at, tempus feugiat enim. Morbi eu dolor metus. Pellentesque vitae purus sit amet nisi vulputate egestas at at urna. Fusce quam lacus, posuere et tortor eu, aliquet mollis nisi. Maecenas in rhoncus libero. Mauris laoreet risus et bibendum cursus. Nunc convallis nunc non porttitor aliquet. Suspendisse odio elit, commodo ac tincidunt at, tempus feugiat enim. Morbi eu dolor metus. Mauris dictum convallis commodo. Maecenas in rhoncus libero. Mauris laoreet risus et bibendum cursus. Nunc convallis nunc non porttitor aliquet. Suspendisse odio elit, commodo ac tincidunt at, tempus feugiat enim. Morbi eu dolor metus. Pellentesque vitae purus sit amet nisi vulputate egestas at at urna.",
        )


if __name__ == "__main__":
    unittest.main()
