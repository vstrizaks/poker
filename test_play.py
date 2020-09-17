from play import play_poker
import pytest


@pytest.mark.parametrize(
    "board, hands, expected_result",
    [
        (
            "4cKs4h8s7s",
            ["Ad4s", "Ac4d", "As9s", "KhKd", "5d6d"],
            "Ac4d=Ad4s 5d6d As9s KhKd",
        ),
        (
            "3c5dAdKsQh",
            ["6c3s", "5c7d", "8cKd", "8h4h", "As6d", "4cKc"],
            "8h4h 6c3s 5c7d 4cKc 8cKd As6d",
        ),
        (
            "3c5d5dKsQh",
            ["3c3s", "5c7d", "8cKd", "8h4h", "As6d", "4cKc"],
            "8h4h As6d 4cKc=8cKd 5c7d 3c3s",
        ),
        (
            "3c5d5dKsQh",
            ["3c3s", "5c5d", "8cKd", "8h4h", "As6d", "4cKc"],
            "8h4h As6d 4cKc=8cKd 3c3s 5c5d",
        ),
        (
            "3c5d5dKs3h",
            ["3cJs", "5cJd", "8cKd", "8h4h", "As6d", "4cKc"],
            "8h4h As6d 4cKc 8cKd 3cJs 5cJd",
        ),
        (
            "Qc5d5dKsQh",
            ["QcJs", "5cJd", "8cKd", "8h4h", "As6d", "4cKc"],
            "8h4h As6d 4cKc 8cKd 5cJd QcJs",
        ),
        ("2c3d4d5s6h", ["QcJs", "5cJd"], "5cJd=QcJs",),
        ("2c3dJdKs6h", ["QcJs", "5cQd"], "5cQd QcJs",),
        ("2c3d4dKs6h", ["QcJs", "AcJd"], "QcJs AcJd",),
        ("2c3d4dKs6h", ["5cJs", "5c7d"], "5cJs 5c7d",),
        ("2d3d4dKc6d", ["5dJs", "5c7c"], "5c7c 5dJs",),
        ("3d3d5d5c6d", ["5d6s", "3c6c", "3h6h"], "3c6c=3h6h 5d6s",),
        ("3d3d5d5c6d", ["5d6s", "3c6c", "5h6h", "3h6h"], "3c6c=3h6h 5d6s=5h6h",),
        ("3d3h5d5c6d", ["5h3s", "3c6c", "Jh6h", "3h6h"], "Jh6h 3c6c=3h6h 5h3s",),
        ("2dJdAd5c6c", ["4d6d", "3d7d"], "4d6d 3d7d",),
        ("QdJdAd5c6c", ["2s2s", "2c2c"], "2c2c=2s2s",),
        ("2dJdAd5c6c", ["3s2s", "Qc2c"], "3s2s Qc2c",),
        ("2dJdAdQc6c", ["9s2s", "8c2c"], "8c2c=9s2s",),
        ("2d3d4dQc6d", ["2d5d", "Ac5c"], "Ac5c 2d5d",),
        ("2d3d4dQc6d", ["2d5d", "7d5d"], "2d5d 7d5d",),
        ("2d3d4dQc6d", ["2d5d", "7d5d", "Ad5d"], "2d5d=Ad5d 7d5d",),
        ("2d3d4dQc5d", ["6d5c", "7d6d", "Ad8d"], "Ad8d 6d5c 7d6d",),
        ("2d3d4dQc6c", ["2d6d", "Ac6c"], "Ac6c 2d6d",),
        ("2d3d4dQc6c", ["2d6d", "Ac6c", "Ad5d"], "Ac6c 2d6d Ad5d",),
        ("2d3d4dQc6c", ["2d6d", "Ac6c", "Ad5d"], "Ac6c 2d6d Ad5d",),
        ("2h3h4h5d8d", ["KdKs", "9hJh"], "KdKs 9hJh",),
        ("2h2h4c5d5d", ["2d8s", "4h5h"], "2d8s 4h5h",),
        ("2h2h4c5d5d", ["4h5h", "2d8s"], "2d8s 4h5h",),
        ("2h2h4c4d5d", ["2h2h", "4d4s"], "2h2h 4d4s",),
        ("2h2h4c4d5d", ["2h2h", "4d4s", "4hJh"], "4hJh 2h2h 4d4s",),
        ("JdQdAdKcKd", ["5dJs", "2d7c", "4dJc", "6dQc"], "2d7c 4dJc 5dJs 6dQc",),
        ("2h6h4cKdAd", ["5d3s", "AhAc"], "AhAc 5d3s",),
        (
            "2h6h4cKdAd",
            ["5d3s", "AhAc", "2h2c", "6sQs", "Kh2c"],
            "6sQs Kh2c 2h2c AhAc 5d3s",
        ),
        (
            "7c7h4cKdAd",
            ["7dQs", "7hJc", "7hKc", "6sQs", "Kh2c"],
            "6sQs Kh2c 7dQs=7hJc 7hKc",
        ),
        (
            "7c7h4cKdAd",
            ["7dQs", "7hJc", "7h9c", "6sQs", "Kh2c"],
            "6sQs Kh2c 7dQs=7h9c=7hJc",
        ),
        (
            "7c7h4c2d3d",
            ["7dQs", "7hJc", "7h9c", "6sQs", "Kh2c"],
            "6sQs Kh2c 7h9c 7hJc 7dQs",
        ),
        (
            "7cJh4c2dJd",
            ["7d4s", "7h2c", "7h9c", "6sQs", "Kh2c"],
            "6sQs Kh2c 7d4s=7h2c 7h9c",
        ),
        (
            "7c4h2c4d7d",
            ["QdQs", "7h2c", "7h9c", "6sQs", "Kh2c"],
            "6sQs Kh2c QdQs 7h2c=7h9c",
        ),
        (
            "7c3h2c4d5d",
            ["7dJs", "7hKc", "7hQc", "5sQs", "Kh5c"],
            "5sQs Kh5c 7dJs 7hQc 7hKc",
        ),
        (
            "AcKhJc9d8d",
            ["7d4s", "7hQc", "7h5c", "5sQs", "4h5c"],
            "4h5c=7d4s=7h5c 5sQs=7hQc",
        ),
        (
            "AcKhJcQd2d",
            ["8d4s", "6h4c", "7h4c", "5s4s", "4h3c"],
            "4h3c 5s4s 6h4c 7h4c 8d4s",
        ),
        ("2h5c8sAsKc", ["Qs9h", "KdQh", "3cKh", "Jc6s"], "Jc6s Qs9h 3cKh KdQh",),
        (
            "3d4s5dJsQd",
            ["5c4h", "7sJd", "KcAs", "9h7h", "2dTc", "Qh8c", "TsJc"],
            "9h7h 2dTc KcAs 7sJd TsJc Qh8c 5c4h",
        ),
        (
            "3s7sAhQhTd",
            ["8h4s", "9c4h", "Kd9s", "3hTs", "9h6c", "TcKh", "6sKs", "8cAs", "2c6h"],
            "2c6h 8h4s 9c4h=9h6c 6sKs Kd9s TcKh 8cAs 3hTs",
        ),
        (
            "4c5c6c9cJs",
            ["6hTh", "8d2s", "5h9s", "KcTc", "3d4d", "3s8c", "7hKs", "9h5s"],
            "8d2s 7hKs 3d4d 6hTh 5h9s=9h5s 3s8c KcTc",
        ),
        (
            "2c5h6h9cAs",
            ["Jc8c", "Td7c", "3s2s", "TcKc", "9sTs", "8s4h", "Th6d", "7s8h", "QsAh"],
            "8s4h Td7c Jc8c TcKc 3s2s Th6d 9sTs QsAh 7s8h",
        ),
        ("2h5d6s9sKs", ["QcAc", "6d8c", "4h8h", "6cJs"], "4h8h QcAc 6d8c 6cJs",),
        (
            "9h9sAdAsTd",
            ["7c7h", "Qd5s", "KsKc", "ThAh", "5h3c", "3s3d", "QhTc", "Qc8s", "6c4d"],
            "3s3d=5h3c=6c4d=7c7h Qc8s=Qd5s QhTc KsKc ThAh",
        ),
        (
            "2c4s8cKcKh",
            ["Qd4c", "3h9h", "As9d", "3s6d", "KdAc", "TsTc", "2hTd", "2d8h"],
            "3s6d 3h9h As9d 2hTd Qd4c 2d8h TsTc KdAc",
        ),
        ("3h5dJcJsTc", ["3sQh", "2s5c", "6cAc", "7cKs"], "7cKs 6cAc 3sQh 2s5c",),
    ],
)
def test_poker(board, hands, expected_result):
    actual_result = play_poker(board, hands, test_run=True)
    assert expected_result == actual_result
