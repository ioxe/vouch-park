import unittest
import InputTransformerService


class InputTransformerServiceTest(unittest.TestCase):
    test_cases = [
        [
            [['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','], ['o'], ['P'],
             [',', '.'], ['7'], ['('], ['A'], ['.'], ['M'], ['.'], [' '], ['T'], ['O'], [','], ['6'], ['P'], ['.'],
             [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U'], ['N'], ['D'], ['A'], ['Y'], ['S']],
            [
                "HOUR, PARKING, oP, 7(A.M. TO, 6P., EXCEPT SUNDAYS",
                "HOUR, PARKING, oP.7(A.M. TO, 6P., EXCEPT SUNDAYS"
            ]
        ],
        [
            [['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','], ['o'], ['P'],
             [',', '.'], ['7'], ['('], ['A'], ['.'], ['M'], ['.'], [' '], ['T'], ['O'], [','], ['6'], ['P'], ['.'],
             [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U', 'O', '0'], ['N'], ['D'], ['A'], ['Y'],
             ['S']],

            [
                'HOUR, PARKING, oP, 7(A.M. TO, 6P., EXCEPT SUNDAYS',
                'HOUR, PARKING, oP, 7(A.M. TO, 6P., EXCEPT SONDAYS',
                'HOUR, PARKING, oP, 7(A.M. TO, 6P., EXCEPT S0NDAYS',
                'HOUR, PARKING, oP.7(A.M. TO, 6P., EXCEPT SUNDAYS',
                'HOUR, PARKING, oP.7(A.M. TO, 6P., EXCEPT SONDAYS',
                'HOUR, PARKING, oP.7(A.M. TO, 6P., EXCEPT S0NDAYS'
            ]
        ],
        [
            [['S'], ['T'], ['O'], ['P'], ['P'], ['I'], ['N'], ['G'], [','], [' '], ['0'], ['2'], ['/'], ['0'], ['7'],
             ['/'], ['2'], ['0'], ['2'], ['0'], [' '], ['-'], [' '], ['0'], ['5'], ['/'], ['0'], ['9'], ['/'], ['2'],
             ['0'], ['2'], ['0'], [','], [' '], ['1'], ['1'], [':'], ['3'], ['0'], ['P'], ['M'], [' '], ['-'], [' '],
             ['7'], [':'], ['0'], ['0'], ['A'], ['M'], [','], [' '], ['F'], ['r'], ['i', 'l'], [','], [' '], ['S'],
             ['a', 'u'], ['t'], [','], [' '], ['S'], ['u'], ['n']],

            ['STOPPING,  02/07/2020 - 05/09/2020,  11:30PM - 7:00AM,  Fri,  Sat,  Sun',
             'STOPPING,  02/07/2020 - 05/09/2020,  11:30PM - 7:00AM,  Fri,  Sut,  Sun',
             'STOPPING,  02/07/2020 - 05/09/2020,  11:30PM - 7:00AM,  Frl,  Sat,  Sun',
             'STOPPING,  02/07/2020 - 05/09/2020,  11:30PM - 7:00AM,  Frl,  Sut,  Sun']
        ],
    ]

    def test(self):
        input_transformer_service = InputTransformerService.InputTransformerService()

        for test_case in self.test_cases:
            actual_result = input_transformer_service.transform_input(test_case[0])

            self.assertEqual(test_case[1], self.verify_tree_using_dfs(actual_result, ""))

    def verify_tree_using_dfs(self, node, prev_lines):
        prev_lines += ", " + node.val
        if len(node.children) == 0:
            return [prev_lines.strip(' ,')]

        merged_list = []
        for child in node.children:
            merged_list.extend(self.verify_tree_using_dfs(child, prev_lines))
        return merged_list


if __name__ == '__main__':
    unittest.main()
