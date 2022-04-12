using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualBasic;

namespace QueensProblemImplementation
{
    public class QueensProblem
    {
        public static Boolean IsSafeRook(List<Position> positions, Position rook) 
        {
            bool isOk = true;
            for (int i = 0; i < positions.Count; i++){
                if (positions[i].RowIndex == rook.RowIndex || positions[i].ColumnIndex == rook.ColumnIndex){
                    isOk = false;
                    break;
                }
            }
            return isOk;
        }

        public static Boolean IsSafeQueen(List<Position> positions, Position queen) 
        {
            bool isOk = IsSafeRook(positions, queen);
            for (int i = 0; i < positions.Count; i++){
                if (positions[i].LeftDiagonal() == queen.LeftDiagonal() || positions[i].RightDiagonal() == queen.RightDiagonal()){
                    isOk = false;
                    break;
                }
            }
            return isOk;
        }

        public static int bS;
        public static bool fini;
        public static List<Position> x = new List<Position>();


        public static List<Position> GetQueensProblemSolution(int boardSize) 
        {
            fini = true;
            bS = boardSize;
            if (boardSize < 4){
                return new List<Position>();
            }
            static void Solve (int row, List<Position> pos){
                if (row < bS && fini) {
                    for (int col = 0; col < bS; col++){
                        Position tmp = new Position(row, col);
                        if (IsSafeQueen(pos, tmp)){
                            pos.Add(tmp);
                            Solve(row + 1, pos);
                            pos.RemoveAt(pos.Count-1);
                        }
                    }
                }
                else if (pos.Count == bS) {
                    x = new List<Position>(pos);
                    fini = false;
                }
            }
            Solve(0, new List<Position>());
            return x;
        }
    }
}