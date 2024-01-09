#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use DBI;
my $user = 'root';
my $password = 'payasitos';
my $dsn = "DBI:mysql:database=nuevoescritor;host=localhost;port=3307";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se pudo conectar!");;

$dbh->disconnect;

print "Ingrese el year: ";
my $anio = <STDIN>;
chomp $anio;

my $busqueda = "SELECT * FROM movie WHERE Year = ?";
my $sth      = $dbh->prepare($busqueda);
$sth->execute($anio);

printf "%-9s%-25s%-6s%-7s%-7s\n", "MovieID", "Title", "Year", "Score", "Votes";
print "---------------------------------------------\n";

while (my ($movie_id, $titulo, $ano, $score, $votos) = $sth->fetchrow_array) {
    printf "%-9s%-25s%-6s%-7s%-7s\n", $movie_id, $titulo, $ano, $score, $votos;
}


$sth->finish;
