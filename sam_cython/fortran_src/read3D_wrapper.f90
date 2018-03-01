module reader_wrapper

use iso_c_binding, only: c_double, c_int, c_char

implicit none

contains

subroutine c_reader(filename, strlen, N, the_array) bind(c)
character(c_char), intent(in),dimension(strlen) :: filename
integer(c_int), intent(in) :: strlen
integer(c_int), intent(in) :: N
real(c_double), intent(out) :: the_array(N)
call reader(filename, strlen, N, the_array)
end subroutine

subroutine reader(filename,strlen,N, the_array)
character(c_char), intent(in),dimension(strlen) :: filename
integer(c_int), intent(in) :: strlen
integer(c_int), intent(in) :: N
integer(c_int) :: i
real(c_double), intent(out) :: the_array(N)

print *,filename
the_array(1)= -999.
the_array(2)= -9999.
do i = 3,N
   the_array(i) = i
end do
end subroutine


end module

