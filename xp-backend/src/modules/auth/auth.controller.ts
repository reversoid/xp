import { Body, Controller, Post } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LoginDTO } from './dto/login.dto';
import { RegisterDTO } from './dto/register.dto';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('register')
  async register(@Body() dto: RegisterDTO) {
    await this.authService.register(dto);
  }

  @Post('login')
  async login(@Body() dto: LoginDTO) {
    await this.authService.login(dto);
  }
}
