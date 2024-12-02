using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace loginpagesw
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            
        }
        // Event handler for the Log In button click
        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            string username = UsernameTextBox.Text;
            string password = PasswordBox.Password;

            // Basic login logic (you can replace this with your own logic)
            if (string.IsNullOrWhiteSpace(username) || string.IsNullOrWhiteSpace(password))
            {
                MessageBox.Show("Please enter both Username and Password.", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
            else
            {
                // Simulate a successful login (replace with actual validation)
                if (username == "admin" && password == "password")
                {
                    MessageBox.Show("Login Successful!", "Success", MessageBoxButton.OK, MessageBoxImage.Information);
                }
                else
                {
                    MessageBox.Show("Invalid Username or Password.", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        // Event handler for the Forgot Password link
        private void ForgotPassword_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Forgot Password clicked. Implement your password recovery logic here.", "Forgot Password");
        }

        // Event handler for the Sign Up link
        private void SignUp_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Sign Up clicked. Implement your sign-up logic here.", "Sign Up");
        }
    }
}