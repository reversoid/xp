import {
  Body,
  Controller,
  Get,
  Post,
  Query,
  ValidationPipe,
} from '@nestjs/common';
import { AuthService, UserExistsException } from './auth.service';
import { LoginDTO } from './dto/login.dto';
import { RegisterDTO } from './dto/register.dto';
import { IsRegisteredQueryDTO } from './dto/is-registered.query.dto';
import {
  ApiBadRequestResponse,
  ApiNotImplementedResponse,
  ApiOperation,
  ApiResponse,
  ApiTags,
} from '@nestjs/swagger';
import { IsRegisteredByTgId } from './dto/responses/IsRegisteredByTGIDResponse';

@ApiTags('Auth')
@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @ApiOperation({ description: 'Register User' })
  @ApiBadRequestResponse({ type: UserExistsException })
  @Post('register')
  async register(@Body() dto: RegisterDTO) {
    await this.authService.register(dto);
  }

  @ApiOperation({ description: 'Check if user registered by Telegram ID' })
  @ApiResponse({ description: 'Result', type: IsRegisteredByTgId })
  @Get('is_registered_tg')
  async isRegistered(
    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { tg_user_id }: IsRegisteredQueryDTO,
  ) {
    const registered = await this.authService.isRegisteredTg(tg_user_id);
    return { registered };
  }

  @ApiOperation({ description: 'Login user' })
  @ApiNotImplementedResponse({ description: 'Method is not implemented' })
  @Post('login')
  async login(@Body() dto: LoginDTO) {
    await this.authService.login(dto);
  }
}
