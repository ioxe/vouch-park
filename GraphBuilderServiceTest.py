import unittest
import GraphBuilderService


class GraphBuilderServiceTest(unittest.TestCase):
    test_cases = [
        [
            [['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','], ['o'], ['P'],
             [',', '.'], ['7'], ['('], ['A'], ['.'], ['M'], ['.'], [' '], ['T'], ['O'], [','], ['6'], ['P'], ['.'],
             [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U'], ['N'], ['D'], ['A'], ['Y'], ['S']],
            {1: 'HOUR', 2: 'PARKING', 3: 'oP', 4: '7(A.M. TO', 5: '6P.', 6: 'EXCEPT SUNDAYS', 7: 'oP.7(A.M. TO'},
            {1: {2}, 2: {3, 7}, 3: {4}, 4: {5}, 5: {6}, 6: set(), 7: {5}}
        ],
        [
            [['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','], ['o'], ['P'],
             [',', '.'], ['7'], ['('], ['A'], ['.'], ['M'], ['.'], [' '], ['T'], ['O'], [','], ['6'], ['P'], ['.'],
             [','], ['E'], ['X'], ['C'], ['E'], ['P'], ['T'], [' '], ['S'], ['U', 'O', '0'], ['N'], ['D'], ['A'], ['Y'],
             ['S']],
            {1: 'HOUR', 2: 'PARKING', 3: 'oP', 4: '7(A.M. TO', 5: '6P.', 6: 'EXCEPT SUNDAYS', 7: 'EXCEPT SONDAYS',
             8: 'EXCEPT S0NDAYS', 9: 'oP.7(A.M. TO'},
            {1: {2}, 2: {9, 3}, 3: {4}, 4: {5}, 5: {8, 6, 7}, 6: set(), 7: set(), 8: set(), 9: {5}}
        ],
        [
            [['2'], [' '], ['H'], ['O'], ['U'], ['R'], [','], ['P'], ['A'], ['R'], ['K'], ['I'], ['N'], ['G'], [','],
             ['o'], ['P'], ['.'], [' '], ['(', '7'], ['A'], ['.'], [' '], ['M'], ['.'], ['T'], ['O'], [','], ['E', '6'],
             ['X'], ['C', 'P'], ['E', '.'], ['P', 'M'], ['T', '.'], [','], ['S'], ['U'], ['N'], ['D'], ['A'], ['Y'],
             ['S']],
            {1: '2 HOUR', 2: 'PARKING', 3: 'oP. (A. M.TO', 4: 'EXCEPT', 5: 'SUNDAYS', 6: 'EXCEP.', 7: 'EXCEMT',
             8: 'EXCEM.', 9: 'EXC.PT', 10: 'EXC.P.', 11: 'EXC.MT', 12: 'EXC.M.', 13: 'EXPEPT', 14: 'EXPEP.',
             15: 'EXPEMT', 16: 'EXPEM.', 17: 'EXP.PT', 18: 'EXP.P.', 19: 'EXP.MT', 20: 'EXP.M.', 21: '6XCEPT',
             22: '6XCEP.', 23: '6XCEMT', 24: '6XCEM.', 25: '6XC.PT', 26: '6XC.P.', 27: '6XC.MT', 28: '6XC.M.',
             29: '6XPEPT', 30: '6XPEP.', 31: '6XPEMT', 32: '6XPEM.', 33: '6XP.PT', 34: '6XP.P.', 35: '6XP.MT',
             36: '6XP.M.', 37: 'oP. 7A. M.TO'},
            {1: {2}, 2: {3, 37},
             3: {4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                 32, 33, 34, 35, 36}, 4: {5}, 5: set(), 6: {5}, 7: {5}, 8: {5}, 9: {5}, 10: {5}, 11: {5}, 12: {5},
             13: {5}, 14: {5}, 15: {5}, 16: {5}, 17: {5}, 18: {5}, 19: {5}, 20: {5}, 21: {5}, 22: {5}, 23: {5}, 24: {5},
             25: {5}, 26: {5}, 27: {5}, 28: {5}, 29: {5}, 30: {5}, 31: {5}, 32: {5}, 33: {5}, 34: {5}, 35: {5}, 36: {5},
             37: {4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                  32, 33, 34, 35, 36}}
        ],
        [
            [['S'], ['T'], ['O'], ['P'], ['P'], ['I'], ['N'], ['G'], [','], [' '], ['0'], ['2'], ['/'], ['0'], ['7'],
             ['/'], ['2'], ['0'], ['2'], ['0'], [' '], ['-'], [' '], ['0'], ['5'], ['/'], ['0'], ['9'], ['/'], ['2'],
             ['0'], ['2'], ['0'], [','], [' '], ['1'], ['1'], [':'], ['3'], ['0'], ['P'], ['M'], [' '], ['-'], [' '],
             ['7'], [':'], ['0'], ['0'], ['A'], ['M'], [','], [' '], ['F'], ['r'], ['i', 'l'], [','], [' '], ['S'],
             ['a', 'u'], ['t'], [','], [' '], ['S'], ['u'], ['n']],
            {1: 'STOPPING', 2: ' 02/07/2020 - 05/09/2020', 3: ' 11:30PM - 7:00AM', 4: ' Fri', 5: ' Sat', 6: ' Sun', 7: ' Sut', 8: ' Frl'},
            {1: {2}, 2: {3}, 3: {8, 4}, 4: {5, 7}, 5: {6}, 6: set(), 7: {6}, 8: {5, 7}}
        ],
    ]

    def test(self):
        graph_builder_service = GraphBuilderService.GraphBuilderService()

        for test_case in self.test_cases:
            vertices, edges = graph_builder_service.transform_array_to_graph(test_case[0])
            self.assertEqual(test_case[1], vertices)
            self.assertEqual(test_case[2], edges)


if __name__ == '__main__':
    unittest.main()
